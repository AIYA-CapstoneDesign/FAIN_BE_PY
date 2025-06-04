# FastAPI 앱 진입점
from fastapi import FastAPI
from app.api.fall_report_api import router

app = FastAPI (
    title = "Python GPT API Server",
    description="FastAPI + LangChain기반 GPTServer",
    version="1.0.0",
    )

# router 등록
app.include_router(router)
