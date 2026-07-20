from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title="AI Knowledge Assistant API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "AI Knowledge Assistant API is running"
    }


print(settings.database_url)