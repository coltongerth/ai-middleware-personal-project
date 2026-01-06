from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from models.sentiment_model import SentimentModel
from utils.auth import authenticate

router = APIRouter()
model = SentimentModel()

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    confidence: float
    user_id: str
    tier: str

@router.post("/", response_model=SentimentResponse)
def analyze_sentiment(
    request: Request,
    payload: SentimentRequest,
    user=Depends(authenticate)
):
    result = model.predict(payload.text)

    return {
        **result,
        "user_id": user["user_id"],
        "tier": user["tier"]
    }