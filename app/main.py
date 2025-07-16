from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine, Base
from .routes import router

app = FastAPI(title="SansManagement API")

origins = [
    "http://localhost:3000",  # Local dev
    "https://sansmanagement-frontend.vercel.app/",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Include all routes
app.include_router(router)
