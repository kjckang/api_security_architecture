from fastapi import FastAPI, Depends, HTTPException
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
#load_dotenv()

app = FastAPI()

# Allow Angular frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Adjust based on frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get API key from environment variable
#API_KEY = os.getenv("API_KEY")
API_KEY = "KC"

def get_api_key():
    """Retrieve API key securely"""
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API Key not found")
    return API_KEY

@app.get("/secure-data")
def get_secure_data(api_key: str = Depends(get_api_key)):
    """Secure endpoint that requires API key"""
    return {"message": "This is secure data", "api_key": api_key}