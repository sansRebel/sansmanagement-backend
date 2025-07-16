
from fastapi import FastAPI
from . import models
from .database import engine, Base
from .routes import router

app = FastAPI(title="SansManagement API")

# Run this at startup to create tables
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Include all contact routes
app.include_router(router)
