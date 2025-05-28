# FastAPI 앱 진입점
from fastapi import FastAPI
from app.api import router

app = FastAPI (
    title = "RAG GPT API Server",
    description="FastAPI + LangChain기반 GPT RAG Server",
    version="0.1.0",
    )

# router 등록
app.include_router(router)