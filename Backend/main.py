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
# TODO [x] Conectar con base de datos
from fastapi import FastAPI
from config import HOST, PORT, ALLOWED_ORIGINS, ALLOW_CREDENTIALS, ALLOW_METHODS, ALLOW_HEADERS
from contextlib import asynccontextmanager
from database.mongodb import MongoDB
from routers import chatbot
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicializar la conexión a la base de datos al iniciar la aplicación
    await MongoDB.connect_db()
    yield
    # Cerrar la conexión a la base de datos al finalizar la aplicación
    await MongoDB.close_db()

# Crear la instancia principal de FastAPI
app = FastAPI(
    title="Hotel Quinchamalí Chatbot API",
    lifespan = lifespan
    )

#Permite solicitudes desde otros orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS,
)

# Incluir el router del chatbot
app.include_router(chatbot.router)

# Ejecutar uvicorn si se ejecuta el archivo
if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)