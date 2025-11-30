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