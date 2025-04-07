# app/routers/chat_router.py
from fastapi import APIRouter, HTTPException
# APIRouter: FastAPI에서 라우팅을 모듈 단위로 관리할 수 있게 해주기 
# 즉, main.py에 모든 경로를 정의하지 않고, 따로 라우팅 파일(chat_router.py)로 분리할 수 있게 도와줌
# HTTPException: 예외 발생 시 HTTP 상태 코드와 메시지를 클라이언트에 보낼 수 있도록 해준다

from pydantic import BaseModel
# FastAPI는 데이터 검증을 위해 Pydantic이라는 라이브러리를 사용
# BaseModel을 상속받은 클래스를 만들면 요청(body)로 들어온 데이터를 자동으로 검증하고 처리해줌

from app.services.Hugface_service import HuggingFaceSummaryService
# app\services\Hugface_service.py의 HuggingFaceSummaryService를 임포트하기


router = APIRouter(prefix="/chat", tags=["Chatbot"])
# APIRouter() 인스턴스를 생성해서 이 파일에서 사용할 라우터를 만들기
# prefix="/chat" → 이 파일 안에 정의되는 모든 경로는 기본적으로 /chat으로 시작하기
# tags=["Chatbot"] → 자동 문서화(/docs)에서 이 라우터에 붙는 태그

class ChatRequest(BaseModel):
    message: str
# 클라이언트가 보낼 JSON은 반드시 다음처럼 생겨야 함


@router.post("/message")
async def get_chat_response(request: ChatRequest):
    # 이 부분은 POST /chat/message 요청이 들어올 때 실행되는 API 핸들러
    # 요청 본문은 ChatRequest로 받고, 그 안에 들어있는 message를 처리함
    try:
        hugface_service = HuggingFaceSummaryService() # 인스턴스 생성,이 인스턴스는 요약 모델(T5 등)을 로드하고, 입력을 요약하는 역할
        response = hugface_service.generate_summary(request.message) 
        # request.message → 유저가 보낸 텍스트
        # generate_summary() → 이 텍스트를 요약해서 결과 문자열을 반환
        return {"response": response} # json형식으로 반환, 예) {"response": "요약된 문장"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    # 만약 모델이 없거나, 에러가 나면 500 서버 에러로 예외를 클라이언트에게 반환
    # 출력 예시) {"detail": "모델을 로드할 수 없습니다."}


