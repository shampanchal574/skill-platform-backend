import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ.get("postgresql://skill_platform_user:O7eLickUoKyk8i9iWQAPCIQWWceUIDjZ@dpg-d5fnjb6r433s73b4cv20-a/skill_platform")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend + DB connected"}

@app.get("/health")
def health():
    return {"status": "ok"}
