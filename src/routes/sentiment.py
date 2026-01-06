from fastapi import APIRouter, Depends, Request, HTTPException
from pydantic import BaseModel
from models.sentiment_model import SentimentModel
from utils.auth import authenticate
from utils.limits import TIER_LIMITS

router = APIRouter()
model = SentimentModel()

class SentimentRequest(BaseModel):
    text: str

@router.post("/")
def analyze_sentiment(
    request: Request,
    payload: SentimentRequest,
    user=Depends(authenticate)
):
    tier = user["tier"]
    limits = TIER_LIMITS[tier]

    if len(payload.text) > limits["max_chars"]:
        raise HTTPException(
            status_code=403,
            detail=f"{tier} tier allows max {limits['max_chars']} characters"
        )

    result = model.predict(payload.text)

    return {
        **result,
        "tier": tier
    }