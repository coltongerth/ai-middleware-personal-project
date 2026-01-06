from fastapi import Header, HTTPException, Request
from typing import Optional

# TEMP storage — replace with DB later
API_KEYS = {
    "free-key-123": {
        "user_id": "user_free_1",
        "tier": "free",
    },
    "premium-key-abc": {
        "user_id": "user_premium_1",
        "tier": "premium",
    },
}


def authenticate(
    request: Request,
    x_api_key: Optional[str] = Header(default=None)
):
    if not x_api_key:
        raise HTTPException(
            status_code=401,
            detail="Missing API key"
        )

    key_data = API_KEYS.get(x_api_key)

    if not key_data:
        raise HTTPException(
            status_code=403,
            detail="Invalid API key"
        )

    request.state.user = key_data

    return key_data