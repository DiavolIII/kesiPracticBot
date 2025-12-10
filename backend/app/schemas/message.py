from pydantic import BaseModel

class MessageCreate(BaseModel):
    text: str

class MessageResponse(BaseModel):
    id: int
    sender: str
    text: str

    class Config:
        from_attributes = True