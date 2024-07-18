from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.prepwhub
user_collection = database.get_collection("users")
article_collection = database.get_collection("articles")
