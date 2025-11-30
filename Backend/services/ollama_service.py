import requests
from config import OLLAMA_URL, MODEL_NAME, TEMPERATURE, TIMEOUT
from prompts.hotel_info import INFO_HOTEL

def preguntar_chatbot(pregunta):
    url = OLLAMA_URL
    payload = {
        "model": MODEL_NAME,
        "prompt": f"{INFO_HOTEL}\n\nCliente: {pregunta}\nAsistente:",
        "stream": False,
        "temperature": TEMPERATURE
    }

    try:
        response = requests.post(url, json=payload, timeout= TIMEOUT)
        response.raise_for_status()
        resultado = response.json()
        return resultado.get("response")

    except requests.exceptions.ConnectionError:
        return "Error: No se puede conectar al chatbot, contacte con personal"
    
    except requests.exceptions.Timeout:
        return "Error: La solicitud al chatbot ha excedido el tiempo de espera"

    except Exception as error:
        return f"Error al hace la consulta: {str(error)}"