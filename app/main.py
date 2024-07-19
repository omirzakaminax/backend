from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from starlette.middleware.cors import CORSMiddleware

from app.auth import auth_router
from app.database import article_collection, uri
from app.models import Article
from app.routes import articles

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tls=True, tlsAllowInvalidCertificates=True)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("An error occurred while connecting to MongoDB: ", e)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(auth_router)
app.include_router(articles.router)


# app.include_router(universities.router)
# app.include_router(calendar.router)
# app.include_router(pomodoro.router)
# app.include_router(messages.router)
# app.include_router(quotes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to PrepWHub"}
