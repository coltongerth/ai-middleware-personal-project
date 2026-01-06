from fastapi import APIRouter, Depends
from utils.auth import authenticate

router = APIRouter(prefix="/auth")

@router.get("/validate")
def validate(user=Depends(authenticate)):
    return {
        "status": "ok",
        "user_id": user["user_id"],
        "tier": user["tier"],
    }