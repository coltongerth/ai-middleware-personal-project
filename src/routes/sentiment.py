from fastapi import APIRouter
from pydantic import BaseModel
from models.sentiment_model import SentimentModel

router = APIRouter()
model = SentimentModel()  # single instance

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    confidence: float

@router.post("/", response_model=SentimentResponse)
def analyze_sentiment(request: SentimentRequest):
    return model.predict(request.text)