# 사전설치 : pip install fastapi uvicorn pandas numpy scikit-learn tensorflow 
# 사전설치 : pip install sqlalchemy pymysql python-dotenv pydantic requests
# uvicorn: FastAPI 앱을 실행시키는 서버
import uvicorn

# FastAPI 클래스 및 모듈 가져오기
from fastapi import FastAPI

# app하위의 routers폴더에서 불러오기
from app.routers import chat_router2

# FastAPI 애플리케이션 인스턴스 생성
# title과 description은 docs 페이지에 표시됨
app = FastAPI(
    title="Chatbot API", description="Hugging Face 기반 요약 챗봇 서비스"
)

# /chat/message 같은 라우트를 app에 등록
# chat_router.router는 APIRouter 인스턴스임
app.include_router(chat_router2.router)

# 루트 경로를 (/)로 정의 예) localhost:8000/
@app.get("/")
async def root():
    return {"message": "Chatbot API Running"}

# 이 파일이 메인으로 실행될 경우 서버 실행
# reload=True는 코드 변경 시 자동으로 서버를 재시작해줌 (개발용)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)