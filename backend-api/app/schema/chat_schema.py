from pydantic import BaseModel
# BaseModel을 상속한 클래스를 만들면, 그것이 하나의 데이터 스키마

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str