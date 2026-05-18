from fastapi import FastAPI

from app.api.routes.chat import router as chat_router
from app.middleware.logging_middleware import LoggingMiddleware

app = FastAPI(
    title="AI Prompt Firewall",
    version="1.0.0",
)

app.add_middleware(LoggingMiddleware)

app.include_router(chat_router)


@app.get("/health")
async def health_check() -> dict:
    return {"status": "healthy"}