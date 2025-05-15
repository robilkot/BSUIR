import logging
from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from datetime import datetime
from model.model import *

app = FastAPI(title="NLP Processing API", description="API for Russian text processing")

logger = logging.getLogger('uvicorn.info')


# Request models
class TextRequest(BaseModel):
    text: str


class SentenceRequest(BaseModel):
    text: str


class SyntaxResponse(BaseModel):
    tokens: list[Syntax]

class MorphologyResponse(BaseModel):
    tokens: list[Morphology]

class SemanticsResponse(BaseModel):
    tokens: list[Semantics]

# Response models
class SentenceResponse(BaseModel):
    text: str
    tokens: List[SentenceToken]


class SentencesResponse(BaseModel):
    sentences: List[SentenceResponse]


@app.post("/text-to-sentences", response_model=SentencesResponse)
async def split_into_sentences(request: TextRequest):
    """Split text into individual sentences"""
    try:
        sentences = text_to_sentences(request.text)

        response_sentences = []
        for sentence in sentences:
            response_sentence = SentenceResponse(text=sentence.text, tokens=sentence.tokens)
            response_sentences.append(response_sentence)

        # logger.info(str(response_sentences).encode('utf-8').decode('utf-8'))
        return SentencesResponse(sentences=response_sentences)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/parse-morphology", response_model=MorphologyResponse)
async def parse_sentence_morphology(request: SentenceRequest):
    try:
        logger.info(str(request))

        result = parse_morphology(request.text)

        return MorphologyResponse(tokens=result.tokens)
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/parse-syntax", response_model=SyntaxResponse)
async def parse_sentence_syntax(request: SentenceRequest):
    try:
        logger.info(str(request))

        result = parse_syntax(request.text)

        return SyntaxResponse(tokens=result.tokens)
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/parse-semantics", response_model=SemanticsResponse)
async def parse_sentence_semantics(request: SentenceRequest):
    try:
        semantics_result = parse_semantics(request.text)

        return SemanticsResponse(tokens=semantics_result.tokens)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/get-word-semantics", response_model=ObjectDescription)
async def parse_sentence_syntax(request: SentenceRequest):
    try:
        logger.info(str(request))

        result = get_words_semantics(request.text)

        return result
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def get_health():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}