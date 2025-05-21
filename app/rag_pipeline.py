# GPT + 벡터 검색 조합 처리 (RAG 핵심)
from app.gpt_client import ask_gpt

def run_rag(question:str) -> str:
    return ask_gpt(question)