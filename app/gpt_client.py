# OpenAI GPT API 호출 모듈
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() #.env 불러오기

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) #api_key를 인자로 넣어 인증해주고, OpenAI 클라이언트 초기화
#client 객체로 GPT모델과의 모든 통신을 담당

#question(문자열) 을 받아서 GPT에게 전달하고, 응답을 문자열로 반환하는 함수
def ask_gpt(question: str) -> str:
    response = client.chat.completions.create( #client 객체를 통해 GPT의 chat completion endpoint 호출
        model="gpt-4.1",
        messages=[
            {"role":"system","content":"당신은 유용한 AI 비서입니다."}, #system : gpt의 성격을 설정하는 안내 메세지
            {"role":"user","content": question} #사용자의 실제 질문(question)
        ],
        temperature=0.7 #출력의 랜덤성을 조절하는 파라미터
    )
    return response.choices[0].message.content #여러 choices중에서 첫번째 응답을 가져옴