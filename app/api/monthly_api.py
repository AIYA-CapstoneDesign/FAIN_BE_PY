# FastAPI 라우팅 정의
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from datetime import date, datetime
from app.gpt_client import call_month_report_gpt
import json

router = APIRouter() #이 모듈의 라우터(경로 모음)을 생성

class MonthlyReportRequest(BaseModel):
    # 환자 기본정보
    name : str
    birth : date
    height : str
    weight : str
    medicine : str
    disease : str
    allergic : str

    # count정보
    fallCount : int
    hCount : int
    pCount : int


    # 과거 리포트들
    monthlyReportHistories : List[str]

@router.post("/month")
async def get_monthreport(request: MonthlyReportRequest):
    monthreports = '\n'.join(['- ' + h for h in request.monthlyReportHistories])
    prompt = f"""
            [리포트 형식]
            {request.name}님은 이번 달 현재까지 {request.fallCount}번의 낙상이 있었습니다.
            - 119 이송횟수와 자체조치횟수를 비교하여 판단하기
            - 과거 리포트들과의 비교
            - 기저질환과 알러지,약 정보를 바탕으로 생활습관과, 병원검진주기등 건강 조언을 해주기

            [환자 정보]
            이름: {request.name}, 생년월일: {request.birth}
            키/몸무게: {request.height}cm / {request.weight}kg
            기저질환: {request.disease}, 약: {request.medicine}, 알러지: {request.allergic}
            119이송횟수 : {request.hCount}, 자체조치횟수 : {request.pCount}
            [과거 리포트 참고] : {monthreports}
                """
    result = call_month_report_gpt(prompt)

    try:
        # 1차: result 자체가 JSON 문자열이라면 파싱
        parsed = json.loads(result)

        # 2차: 내부에 또 중첩된 JSON이 문자열로 있으면 한 번 더 파싱
        if isinstance(parsed, dict) and "aiComment" in parsed:
            inner = json.loads(parsed["aiComment"])
            report_text = inner["aiComment"]
        else:
            report_text = parsed.get("aiComment") or parsed.get("report") or result

    except Exception:
        # 파싱 실패하면 그냥 원본 리턴
        report_text = result

    # 🎯 오직 순수 문자열만 Spring으로 넘김
    return report_text
    
