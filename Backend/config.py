#Configuración de CORS 
ALLOWED_ORIGINS = ["http://localhost:3000"]
ALLOW_CREDENTIALS = True
ALLOW_METHODS = ["*"]
ALLOW_HEADERS = ["*"]

#Configuración del modelo
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:1b"
TEMPERATURE = 0.7
TIMEOUT = 30

#Configuracion del servidor
HOST = "0.0.0.0"
PORT = 8000

#MongoDB 
MONGODB_URL = "mongodb://localhost:27017/"
DATABASE_NAME = "hotel_quinchamali"
COLLECTION_NAME = "chat_historial"