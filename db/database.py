from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

# MongoDB
mongodb_url = f"mongodb://{settings.MONGODB_HOST}:{settings.MONGODB_PORT}"
client = AsyncIOMotorClient(mongodb_url)
database = client.rss
users_collection = database.get_collection("users")
