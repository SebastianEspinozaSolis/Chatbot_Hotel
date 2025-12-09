"""
La función `chatbot_endpoint` en esta aplicación FastAPI maneja las solicitudes de chat entrantes,
valida el mensaje y devuelve una respuesta de un servicio de chatbot.

El parámetro `request` en la función `chatbot_endpoint` es de tipo `ChatRequest`,
que es un modelo de Pydantic definido en el módulo `models.schemas`. Representa el cuerpo de la
solicitud del endpoint `/chatbot` y contiene un campo `message`.
ChatRequest
El endpoint `/chatbot` devuelve un objeto `ChatResponse` con la respuesta del servicio
de chatbot y un estado de "success".
"""

from fastapi import APIRouter, HTTPException
from models.schemas import ChatRequest, ChatResponse
from services.ollama_service import preguntar_chatbot
from services.chat_history_service import guardar_historial_chat
from database.mongodb import get_collection

router = APIRouter(prefix="/api", tags=["chatbot"])

@router.post("/chatbot")
async def chatbot_endpoint(request: ChatRequest):
    if not request.message or not request.message.strip():
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")
    
    respuesta = preguntar_chatbot(request.message)

    try:
        await guardar_historial_chat(
            mensaje_usuario=request.message,
            respuesta_chatbot=respuesta
        )
    except Exception as e:
        print(f"Error al guardar el historial del chat: {str(e)}")

    return ChatResponse(
        response=respuesta,
        status="success"
    )

