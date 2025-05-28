# 1. Python 3.11 이미지 사용
FROM python:3.11-slim
# 2. 작업 디렉토리 생성
WORKDIR /app
# 3. 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# 4. 앱 소스 복사
COPY . .
# 5. 실행 명령 (예: main.py기준)
CMD ["python","main.py"]