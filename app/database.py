
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get the connection string from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the async database engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create session factory for async interaction
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base class for models
Base = declarative_base()

# Dependency for routes to access DB session
async def get_db():
    async with SessionLocal() as session:
        yield session
