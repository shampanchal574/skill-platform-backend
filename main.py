from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create app FIRST
app = FastAPI()

# Add middleware AFTER app exists
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Skill Platform Backend Running"}

@app.get("/health")
def health():
    return {"status": "ok"}
