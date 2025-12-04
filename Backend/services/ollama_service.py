"""
La función `preguntar_chatbot` envía una pregunta a un chatbot utilizando un modelo y parámetros
especificados, manejando diferentes tipos de excepciones que pueden ocurrir durante el proceso.

La función `preguntar_chatbot` recibe una pregunta como entrada y la envía a una
API de chatbot para obtener una respuesta. Aquí se describen los parámetros utilizados en la función:
La función `preguntar_chatbot` devuelve la respuesta del chatbot basada en la pregunta
proporcionada. Si la solicitud es exitosa, devuelve la respuesta del chatbot. Si ocurre un error de
conexión, devuelve un mensaje indicando que no se puede conectar con el chatbot y aconseja contactar
al personal. Si la solicitud expira, devuelve un mensaje indicando que la solicitud al chat ha
excedido el tiempo de espera.
"""
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