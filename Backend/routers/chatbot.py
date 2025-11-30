from fastapi import APIRouter, HTTPException
from models.schemas import ChatRequest, ChatResponse
from services.ollama_service import preguntar_chatbot

router = APIRouter(prefix="/api")

@router.post("/chatbot")
async def chatbot_endpoint(request: ChatRequest):
    if not request.message or not request.message.strip():
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")
    
    respuesta = preguntar_chatbot(request.message)

    return ChatResponse(
        response=respuesta,
        status="success"
    )