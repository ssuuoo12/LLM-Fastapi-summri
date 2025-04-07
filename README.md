# LLM 기반 FastAPI사용한 핵심봇

FastAPI + Spring Boot 기반 챗봇 시스템으로, 사용자 텍스트 입력을 바탕으로 요약한 텍스트를 답변해주는 핵심봇입니다.

Hugging face모델 : https://huggingface.co/lcw99/t5-base-korean-text-summary
---

### 주요 기능

- 사용자가 입력한 텍스트 요약
---

## 기술 스택

| 영역       | 기술 |
|------------|------|
| 프론트     | JSP, HTML, CSS |
| 백엔드     | Spring Boot, FastAPI |
| AI         | Python, Huggingface |
| 배포       | Localhost (시연용) |

---

## 실행 방법

### FastAPI 서버 실행 (VSCode)

```bash
cd FastAPI
uvicorn main:app --reload
// or
python main.py
```
#### main.py에 설정한 포트로 실행하여 모델이 잘 작동하는지 확인 

### Spring boot 서버 실행 (VSCode)
refresh gradle => 서버 restart => localhost:8080로 프로토타입(화면) 출력

사용자 최대 입력 토큰 수 : 512

출력은 최대 100토큰까지 생성하게 제한
