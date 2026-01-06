import time
from fastapi import HTTPException

# { api_key: [timestamps] }
REQUEST_LOG = {}

def rate_limit(api_key: str, tier: str, limit: int | None):
    if limit is None:
        return  # unlimited

    now = time.time()
    window_start = now - 60

    timestamps = REQUEST_LOG.get(api_key, [])
    timestamps = [t for t in timestamps if t > window_start]

    if len(timestamps) >= limit:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded"
        )

    timestamps.append(now)
    REQUEST_LOG[api_key] = timestamps