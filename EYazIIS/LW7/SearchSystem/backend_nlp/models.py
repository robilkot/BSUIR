from enum import Enum, auto
from typing import List, Optional

from pydantic import BaseModel, AliasChoices, Field, ConfigDict


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
