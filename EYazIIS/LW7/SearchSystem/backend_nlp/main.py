from collections import Counter
from enum import auto, Enum
from functools import lru_cache
import threading

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field, AliasChoices
from typing import List, Optional


# Thread-safe initialization
class NatashaComponents:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def initialize(self):
        if not self._initialized:
            from natasha import (
                Segmenter, MorphVocab, NewsEmbedding,
                NewsMorphTagger, NewsSyntaxParser, NewsNERTagger,
                NamesExtractor, DatesExtractor, MoneyExtractor, AddrExtractor
            )

            self.segmenter = Segmenter()
            self.morph_vocab = MorphVocab()
            self.emb = NewsEmbedding()
            self.morph_tagger = NewsMorphTagger(self.emb)
            self.syntax_parser = NewsSyntaxParser(self.emb)
            self.ner_tagger = NewsNERTagger(self.emb)
            self._initialized = True


natasha_components = NatashaComponents()

app = FastAPI(title="Russian Text Processing API", version="1.0.0")


class NERClass(Enum):
    PER = auto()
    LOC = auto()
    ORG = auto()


NERClassDict = {
    'PER': NERClass.PER,
    'LOC': NERClass.LOC,
    'ORG': NERClass.ORG,
}


# Request/Response Models
class TextRequest(BaseModel):
    text: str = Field(validation_alias=AliasChoices('Text', 'text'))
    max_keywords: Optional[int] = Field(default=None, validation_alias=AliasChoices('MaxKeywords', 'maxKeywords'))
    max_entities: Optional[int] = Field(default=None, validation_alias=AliasChoices('MaxEntities', 'maxEntities'))


class NamedEntity(BaseModel):
    model_config = ConfigDict(frozen=True)
    Text: str
    Type: NERClass
    NormalizedText: str | None = None


class KeywordMetadata(BaseModel):
    text: str
    frequency: float


class MetadataResponse(BaseModel):
    entities: List[NamedEntity]
    keywords: List[KeywordMetadata]


# Cache for processed texts to avoid reprocessing identical requests
@lru_cache(maxsize=1000)
def process_text_cached(text: str, max_keywords: int, max_entities: int):
    from natasha import Doc

    natasha_components.initialize()

    doc = Doc(text)
    doc.segment(natasha_components.segmenter)
    doc.tag_morph(natasha_components.morph_tagger)
    doc.parse_syntax(natasha_components.syntax_parser)
    doc.tag_ner(natasha_components.ner_tagger)

    # Optimized keyword extraction
    lemmas = []
    for token in doc.tokens:
        if token.pos not in ['PUNCT']:
            token.lemmatize(natasha_components.morph_vocab)
            lemma = token.lemma.lower()
            lemmas.append(lemma)

    # Use most_common for better performance with Counter
    count_dict = Counter(lemmas)
    total_tokens = len(lemmas)

    keywords = [
        KeywordMetadata(text=lemma, frequency=count / total_tokens)
        for lemma, count in count_dict.most_common(max_keywords)
    ]

    # Optimized NER processing
    entities_set = set()
    for span in doc.spans:
        if span.type != '_':
            span.normalize(natasha_components.morph_vocab)
            entity = NamedEntity(
                Text=doc.text[span.start:span.stop],
                Type=NERClassDict[span.type],
                NormalizedText=span.normal
            )
            # Use hash of the entity for set operations
            entities_set.add(entity)

    entities = list(entities_set)[:max_entities]

    return MetadataResponse(entities=entities, keywords=keywords)


@app.post("/extract-metadata", response_model=MetadataResponse)
async def extract_keywords(request: TextRequest):
    # Set defaults if None
    max_keywords = request.max_keywords or 50
    max_entities = request.max_entities or 20

    # Use cached processing with text length as part of cache key
    cache_key = (request.text, max_keywords, max_entities)
    return process_text_cached(*cache_key)


@app.get("/health")
async def health_check():
    return {"status": "healthy", "cache_info": process_text_cached.cache_info()}


@app.delete("/cache")
async def clear_cache():
    process_text_cached.cache_clear()
    return {"message": "Cache cleared"}


if __name__ == "__main__":
    import uvicorn

    # Pre-initialize Natasha components on startup
    natasha_components.initialize()

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        workers=2
    )