from datetime import datetime
from database.mongodb import get_collection
from config import COLLECTION_NAME  

async def guardar_historial_chat(mensaje_usuario: str, respuesta_chatbot: str):
    """
    Guarda el historial del chat en la base de datos MongoDB.

    Parámetros:
    - mensaje_usuario (str): El mensaje enviado por el usuario.
    - respuesta_chatbot (str): La respuesta generada por el chatbot.
    """
    collection = get_collection(COLLECTION_NAME)
    message = {
        "mensaje_usuario": mensaje_usuario,
        "respuesta_chatbot": respuesta_chatbot,
        "timestamp": datetime.now()
    }
    result = await collection.insert_one(message)
    inserted_id = str(result.inserted_id)
    print(f"Guardado historial en MongoDB, inserted_id={inserted_id}")
    return inserted_id