# OpenAI GPT API 호출 모듈
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() #.env 불러오기

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) #api_key를 인자로 넣어 인증해주고, OpenAI 클라이언트 초기화
#client 객체로 GPT모델과의 모든 통신을 담당

def call_report_gpt(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages= [
            {
                "role":"system",
                "content": "당신은 건강 분석 전문가입니다. 친절한 말투로 일반인이 알기 쉽게 리포트를 250자 이내, 1~2문장으로 간결하게 작성하세요. "

            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text":prompt},
                ]
            }
        ],

        temperature=0.7
    )
    print("GPT 응답 원문:", response.choices[0].message.content)
    return response.choices[0].message.content #여러 choices중에서 첫번째 응답을 가져옴