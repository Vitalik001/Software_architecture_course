from pydantic import BaseModel

class Message(BaseModel):
    text: str


class PostMessage(BaseModel):
    id: str
    text: str