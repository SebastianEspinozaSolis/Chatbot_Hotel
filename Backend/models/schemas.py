# El código anterior define dos modelos de Pydantic, ChatRequest y ChatResponse, con campos para un mensaje y una respuesta, junto con sus respectivos estados.
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    status: str