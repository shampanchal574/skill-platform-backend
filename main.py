import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

app = FastAPI()

# CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- MODELS --------
class SignupRequest(BaseModel):
    name: str
    email: str
    password: str
    role: str  # customer or employer

# -------- ROUTES --------
@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.post("/signup")
def signup(data: SignupRequest):
    return {
        "status": "success",
        "message": "User registered successfully",
        "user": data
    }

@app.post("/login")
def login():
    return {"message": "Login working"}

DATABASE_URL = os.environ.get("DATABASE_URL")

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
