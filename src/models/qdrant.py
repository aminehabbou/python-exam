from pydantic import BaseModel


class QdrantMessagePayload(BaseModel):
    id: int
    object: str
    model: str
    message_text: str
    message_role: str
