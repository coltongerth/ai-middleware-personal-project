from fastapi import FastAPI
from src.routes.sentiment import router as sentiment_router
from src.routes.ui import router as ui_router
from src.routes.login import router as login_router
from src.routes.auth import router as auth_router



app = FastAPI(title="AI Middleware API")

app.include_router(login_router)
app.include_router(auth_router)
app.include_router(ui_router, prefix='/ui')
app.include_router(sentiment_router, prefix="/sentiment")