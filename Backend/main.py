"""
Este archivo configura una aplicación FastAPI para la API del chatbot del Hotel Quinchamalí.

- Se importan las configuraciones del servidor (HOST, PORT) y los parámetros para CORS.
- Se crea la instancia principal de FastAPI.
- Se agrega el middleware CORS para permitir solicitudes desde otros orígenes.
- Se incluye el router del chatbot donde están los endpoints.
- Si el archivo se ejecuta directamente, se inicia el servidor con Uvicorn.

En resumen: este script inicia la API, habilita CORS, registra las rutas del chatbot
y ejecuta el servidor.
"""
# TODO [ ] Conectar con base de datos
from fastapi import FastAPI
from config import HOST, PORT, ALLOWED_ORIGINS, ALLOW_CREDENTIALS, ALLOW_METHODS, ALLOW_HEADERS
from routers import chatbot
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Hotel Quinchamalí Chatbot API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS,
)

app.include_router(chatbot.router)

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)