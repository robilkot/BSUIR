import io
import threading
from collections import Counter
from functools import lru_cache

import librosa
import torch
from fastapi import FastAPI, HTTPException, UploadFile, File
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

from models import *


LANG_ID = "ru"
MODEL_ID = "jonatasgrosman/wav2vec2-large-xlsr-53-russian"
SAMPLES = 5

processor: Wav2Vec2Processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)



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
                NewsMorphTagger, NewsSyntaxParser, NewsNERTagger
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


@app.post("/speech-to-text")
async def speech_to_text(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        audio_bytes = io.BytesIO(contents)

        speech_array, sampling_rate = librosa.load(audio_bytes, sr=16_000)

        inputs = processor(speech_array, sampling_rate=16_000, return_tensors="pt", padding=True)

        with torch.no_grad():
            logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

        predicted_ids = torch.argmax(logits, dim=-1)
        predicted_sentences = processor.batch_decode(predicted_ids)

        return predicted_sentences[0]

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing audio file: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    # Pre-initialize Natasha components on startup
    natasha_components.initialize()

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        workers=1
    )
