from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from datetime import datetime
from model.model import *

app = FastAPI(title="NLP Processing API", description="API for Russian text processing")


# Request models
class TextRequest(BaseModel):
    text: str


class SentenceRequest(BaseModel):
    text: str
    tokens: List[dict]


# Response models
class SentenceResponse(BaseModel):
    text: str
    tokens: List[dict]
    syntax: Optional[dict] = None
    semantics: Optional[dict] = None


class SentencesResponse(BaseModel):
    sentences: List[SentenceResponse]


# Convert SentenceToken to/from dictionary for serialization
def token_to_dict(token: SentenceToken) -> dict:
    return {
        "start_idx": token.start_idx,
        "end_idx": token.end_idx,
        "pos": token.pos,
        "lemma": token.lemma,
        "morph_info": token.morph_info
    }


def dict_to_token(data: dict) -> SentenceToken:
    return SentenceToken(
        start_idx=data["start_idx"],
        end_idx=data["end_idx"],
        pos=data.get("pos"),
        lemma=data.get("lemma"),
        morph_info=data.get("morph_info")
    )


@app.post("/text-to-sentences", response_model=SentencesResponse)
async def split_into_sentences(request: TextRequest):
    """Split text into individual sentences"""
    try:
        sentences = text_to_sentences(request.text)

        response_sentences = []
        for sentence in sentences:
            response_sentence = {
                "text": sentence.text,
                "tokens": [token_to_dict(token) for token in sentence.tokens],
                "syntax": None,
                "semantics": None
            }
            response_sentences.append(response_sentence)

        return SentencesResponse(sentences=response_sentences)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/parse-syntax", response_model=SentenceResponse)
async def parse_sentence_syntax(request: SentenceRequest):
    """Parse syntactic structure of a sentence"""
    try:
        # Convert request data back to Sentence object
        sentence = Sentence(
            text=request.text,
            tokens=list(dict_to_token(token) for token in request.tokens),
            syntax=None,
            semantics=None
        )

        # Process syntax parsing
        syntax_result = parse_syntax(sentence)

        return SentenceResponse(
            text=sentence.text,
            tokens=[token_to_dict(token) for token in sentence.tokens],
            syntax={"tokens": [{"id": token.id,
                                "head_id": token.head_id,
                                "relation": token.relation.name}
                               for token in syntax_result.tokens]}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/parse-semantics", response_model=SentenceResponse)
async def parse_sentence_semantics(request: SentenceRequest):
    """Parse semantic structure of a sentence"""
    try:
        sentence = Sentence(
            text=request.text,
            tokens=list(dict_to_token(token) for token in request.tokens),
            syntax=None,
            semantics=None
        )

        semantics_result = parse_semantics(sentence)

        return SentenceResponse(
            text=sentence.text,
            tokens=[token_to_dict(token) for token in sentence.tokens],
            semantics={"result": str(semantics_result)}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/health")
async def get_health():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}