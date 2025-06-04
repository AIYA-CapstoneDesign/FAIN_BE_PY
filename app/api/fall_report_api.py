# FastAPI 라우팅 정의
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from datetime import date, datetime
from app.gpt_client import call_report_gpt

router = APIRouter() #이 모듈의 라우터(경로 모음)을 생성

class ReportRequest(BaseModel):
    # 환자 기본정보
    name : str
    birth : date
    height : str
    weight : str
    medicine : str
    disease : str
    allergic : str

    # 리포트 정보
    situationTime : datetime

    # 과거 리포트들
    reportHistories : List[str]

@router.post("/report")
async def get_report(request: ReportRequest):
    reports = '\n'.join(['- ' + h for h in request.reportHistories])
    prompt = f"""
             다음 정보를 바탕으로, 이러한 사람이 낙상시 어떤것 때문에 낙상했을지, 그렇다면 즉시 어떤 조치를 취해야할지 추론해줘
             
            조건:
            1. 반드시 250자 이내.
            2. 이름 "{request.name}"을 포함해 3인칭 존칭 사용.
            3. 주변 환경은 언급하지 말 것.
            4. 조치는 구체적이고 즉시 가능한 것으로 작성.
            5. 기저질환, 복용약 두가지 관점에 대해서 모두 응답할 것.
            6. 낙상의 요인이 될 수도 있다는 추상적인 말을 할 것.

            형식:
            [분석] 낙상 원인  
            [조치] 즉시 필요한 조치

            [환자 정보]
            이름: {request.name}, 생년월일: {request.birth}
            키/몸무게: {request.height}cm / {request.weight}kg
            기저질환: {request.disease}, 약: {request.medicine}, 알러지: {request.allergic}

            [과거 리포트 참고]
            {reports}
                """
    result = call_report_gpt(prompt)
    return {"report":result}


    



