from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
    # Probar conexión
    client.admin.command('ping')
    print("✅ MongoDB está corriendo y conectado!")
    
    # Ver bases de datos
    print("Bases de datos:", client.list_database_names())
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("MongoDB no está corriendo o no está instalado")