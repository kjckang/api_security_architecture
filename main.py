## uvicorn main:app --reload

from fastapi import FastAPI, Depends, HTTPException, Request
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
#load_dotenv()

allow_url=["http://localhost:4200"]

app = FastAPI()

# Allow Angular frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_url,  # Adjust based on frontend URL
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
def get_secure_data(request: Request, api_key: str = Depends(get_api_key)):
    """Secure endpoint that requires API key and checks request origin"""
    origin = request.headers.get("origin")
    if origin not in allow_url:
        raise HTTPException(status_code=403, detail=f"Access denied: {origin} is not an allowed domain")
    return {"message": "This is secure data", "api_key": api_key}
