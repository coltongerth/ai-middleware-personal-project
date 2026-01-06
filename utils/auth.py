from fastapi import Header, HTTPException, Request
from typing import Optional
from utils.limits import TIER_LIMITS
from utils.rate_limit import rate_limit

# Dummy API keys
API_KEYS = {
    "free-key-123": {
        "user_id": "user_free_1",
        "tier": "free",
    },
    "premium-key-123": {
        "user_id": "user_premium_1",
        "tier": "premium",
    },
}


def authenticate(
    request: Request,
    x_api_key: Optional[str] = Header(default=None)
):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="Missing API key")

    user = API_KEYS.get(x_api_key)
    if not user:
        raise HTTPException(status_code=403, detail="Invalid API key")

    limits = TIER_LIMITS[user["tier"]]
    rate_limit(
        api_key=x_api_key,
        tier=user["tier"],
        limit=limits["requests_per_minute"]
    )

    request.state.user = user
    return user