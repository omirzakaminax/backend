from fastapi import FastAPI
from app.auth import auth_router
from app.models import Article
from app.database import article_collection

app = FastAPI()

app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to PrepWHub"}

@app.get("/articles")
async def get_articles():
    articles = []
    async for article in article_collection.find():
        articles.append(Article(**article))
    return articles
