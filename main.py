# FastAPI 앱 진입점
from fastapi import FastAPI
from app.api.fall_report_api import router as fall_router
from app.api.monthly_api import router as month_router

app = FastAPI (
    title = "Python GPT API Server",
    description="FastAPI + LangChain기반 GPTServer",
    version="1.0.0",
    )

# router 등록
app.include_router(fall_router)

# month_router 등록
app.include_router(month_router)
