# FastAPI 라우팅 정의
from fastapi import APIRouter,Request
from pydantic import BaseModel
from app.rag_pipeline import run_rag #추후 GPT 호출 함수로 연결할 예정

router = APIRouter() #이 모듈의 라우터(경로 모음)을 생성

class QueryRequest(BaseModel): #/query API의 요청 JSON 구조 정의
    question: str #문자열 필드를 받을 예정

@router.get("/ping") #GET "/ping" API - 서버가 살아있는지 테스트용 API
async def ping(): # 비동기적으로 동작
    return {"message":"pong"}

@router.post("/query") #POST "/query" API - 요청 body에 들어온 JSON데이터를 QueryRequest형태로 자동 파싱
async def query_handler(request: QueryRequest):
    #GPT 처리 함수 호출(일단 Mock 처리)
    answer = run_rag(request.question) #question 값을 run_rag() 함수에 넘겨 응답 받아옴

    return {"question":request.question, "answer":answer} #사용자 질문과 답변을 함께 JSON형식으로 반환