from fastapi import APIRouter, HTTPException, Depends
from app.models import Article
from app.schemas import ArticleCreate
from app.database import article_collection

router = APIRouter(prefix="/articles", tags=["articles"])

@router.get("/")
async def get_articles():
    articles = []
    async for article in article_collection.find():
        articles.append(Article(**article))
    return articles

@router.post("/")
async def create_article(article: ArticleCreate):
    article_dict = article.dict()
    new_article = await article_collection.insert_one(article_dict)
    created_article = await article_collection.find_one({"_id": new_article.inserted_id})
    return Article(**created_article)
