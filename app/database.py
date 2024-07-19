import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db = client.prepwhub
user_collection = db.get_collection("users")
article_collection = db.get_collection("articles")
