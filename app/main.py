import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import products, health_check

app = FastAPI(
    title="Product Comparison Service",
    version="0.0.1",
)

# Load environment variables from .env file
load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI")

if not DATABASE_URI:
    raise ValueError("DATABASE_URI is not set in the environment variables")


# secret key
SECRET_KEY = os.getenv("SECRET_KEY")


# Cross origins
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# endpoint routers
app.include_router(products.router)
app.include_router(health_check.router)
