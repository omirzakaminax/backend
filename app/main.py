from fastapi import FastAPI
from app.routes import articles, universities, calendar, pomodoro, messages, quotes
from app.auth import auth_router
from app.models import Article
from app.database import article_collection
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://omirzakaminax:Amina09@prepwhub.gz5kd1v.mongodb.net/?retryWrites=true&w=majority&appName=prepwhub"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = FastAPI()

app.include_router(auth_router)
app.include_router(articles.router)
app.include_router(universities.router)
app.include_router(calendar.router)
app.include_router(pomodoro.router)
app.include_router(messages.router)
app.include_router(quotes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to PrepWHub"}


@app.get("/articles")
async def get_articles():
    articles = []
    async for article in article_collection.find():
        articles.append(Article(**article))
    return articles
