from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="React FastAPI AI App Backend")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for request validation
class IdeaRequest(BaseModel):
    idea: str

@app.get("/")
async def root():
    return {"message": "Welcome to React FastAPI AI App Backend"}

@app.post("/process-idea/")
async def process_idea(request: IdeaRequest):
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")
    
    try:
        response = requests.post(
            "https://api.openai.com/v1/completions",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
            json={
                "model": "text-davinci-003",
                "prompt": f"Refine this idea: {request.idea}",
                "max_tokens": 100,
            },
        )
        response.raise_for_status()
        return {"refined_idea": response.json()["choices"][0]["text"].strip()}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}