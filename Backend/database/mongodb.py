from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGODB_URL, DATABASE_NAME

class MongoDB:
    client: AsyncIOMotorClient = None

    @classmethod
    async def connect_db(cls):
        try:
            cls.client = AsyncIOMotorClient(MONGODB_URL)
            await cls.client.admin.command('ping')
            print("✅ Conectado a MongoDB")
        except Exception as e:
            print(f"❌ Error al conectar a MongoDB: {e}")
        
    @classmethod
    async def close_db(cls):
        if cls.client:
            cls.client.close()
            print("🔒 Conexión a MongoDB cerrada")
    
    @classmethod
    def get_database(cls):
        return cls.client[DATABASE_NAME]
    
def get_collection(collection_name: str):
    db = MongoDB.get_database()
    return db[collection_name]