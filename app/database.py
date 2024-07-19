import motor.motor_asyncio

uri = ("mongodb+srv://omirzakaminax:Amina09@prepwhub.gz5kd1v.mongodb.net/?retryWrites=true&w=majority&appName=prepwhub"
       "&tls=true")
client = motor.motor_asyncio.AsyncIOMotorClient(uri)
db = client.prepwhub
user_collection = db.get_collection("users")
article_collection = db.get_collection("articles")
