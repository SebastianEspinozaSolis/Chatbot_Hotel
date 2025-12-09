# Modelo Pydantic para representar un mensaje de chat y una respuesta de ejemplo
from datetime import datetime
from pydantic import BaseModel, Field

class ChatMessage(BaseModel):
    mensaje_usuario: str
    respuesta_chatbot: str
    timestamp: datetime = Field(default_factory = datetime.now)

    class Config:
        schema_extra ={
            "example": {
                "mensaje_usuario": "¿Cuáles son los servicios del hotel?",
                "respuesta_chatbot": "Ofrecemos WiFi gratuito, desayuno incluido.",
                "timestamp": "2025-12-04T12:00:00"
            }
        }