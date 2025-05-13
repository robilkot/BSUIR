from typing import Optional, List

from pydantic import BaseModel, Field
from datetime import datetime


class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime


class User(BaseModel):
    name: str
    about: str

class MessageContent(BaseModel):
    images: List[str]
    links: List[str]
    text: Optional[str]

class MessageMetadata(BaseModel):
    sent: datetime
    sender: User

class MessageReactions(BaseModel):
    rating: str

class Message(BaseModel):
    content: MessageContent
    metadata: MessageMetadata
    reactions: Optional[MessageReactions]

class RateMessageRequest(BaseModel):
    message: Message
    rating: str


class ChatRequest(BaseModel):
    session_id: str = Field(default=None)
    message: Message


class ChatResponse(BaseModel):
    session_id: str = Field(default=None)
    message: Message

