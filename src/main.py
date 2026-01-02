from fastapi import FastAPI
from src.routes.sentiment import router as sentiment_router
from src.routes.ui import router as ui_router

app = FastAPI(title="AI Middleware API")

app.include_router(ui_router)
app.include_router(sentiment_router, prefix="/sentiment")