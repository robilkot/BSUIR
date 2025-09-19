from collections import Counter
from enum import auto, Enum

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field, AliasChoices
from typing import List, Optional
from natasha import (
    Doc,
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    NamesExtractor,
    DatesExtractor,
    MoneyExtractor,
    AddrExtractor
)


# Initialize Natasha components
segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)
names_extractor = NamesExtractor(morph_vocab)
dates_extractor = DatesExtractor(morph_vocab)
money_extractor = MoneyExtractor(morph_vocab)
addr_extractor = AddrExtractor(morph_vocab)

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
    max_keywords: Optional[int] = Field(validation_alias=AliasChoices('MaxKeywords', 'maxKeywords'))
    max_entities: Optional[int] = Field(validation_alias=AliasChoices('MaxEntities', 'maxEntities'))


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


@app.post("/extract-metadata", response_model=MetadataResponse)
async def extract_keywords(request: TextRequest):
    doc = Doc(request.text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)

    # Keywords
    lemmas = []
    for token in doc.tokens:
        # if token.pos in ['NOUN', 'ADJ', 'VERB']:
        if token.pos not in ['PUNCT']:
            token.lemmatize(morph_vocab)
            lemma = token.lemma.lower()
            lemmas.append(lemma)

    count_dict = Counter(lemmas)
    keywords = [KeywordMetadata(text=lemma, frequency=count / len(lemmas)) for lemma, count in count_dict.items()]
    keywords.sort(key=lambda metadata: metadata.frequency, reverse=True)
    keywords = keywords[:request.max_keywords]


    # NER
    for span in doc.spans:
        span.normalize(morph_vocab)

    entities = [NamedEntity(Text=doc.text[span.start:span.stop],
                             Type=NERClassDict[span.type],
                             NormalizedText=span.normal)
                 for span in doc.spans if span.type != '_']
    entities = list(set(entities))

    return MetadataResponse(entities=entities, keywords=keywords)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)