# LLM 기반 FastAPI사용한 핵심봇

<p align="center">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white" />
  <img src="https://img.shields.io/badge/huggingface-FF9A00?style=for-the-badge&logo=huggingface&logoColor=white" />
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white" />
</p>

FastAPI + Spring Boot 기반 챗봇 시스템으로, 사용자 텍스트 입력을 바탕으로 요약한 텍스트를 답변해주는 핵심봇입니다.

## 모델 정보
🤗 Hugging Face 모델: [lcw99/t5-base-korean-text-summary](https://huggingface.co/lcw99/t5-base-korean-text-summary)

## 주요 기능
- 사용자가 입력한 텍스트 요약
- 사용자 최대 입력 토큰 수: 512
- 출력은 최대 100토큰까지 생성하게 제한

## 기술 스택

| 영역       | 기술 |
|------------|------|
| 프론트엔드 | JSP, HTML, CSS |
| 백엔드     | Spring Boot, FastAPI |
| AI         | Python, Hugging Face |


## 시스템 구조
![시스템 구조도](./images/system-architecture.png)

## 실행 방법

### FastAPI 서버 실행 (VSCode)
```bash
# 디렉토리 이동
cd FastAPI

# 서버 실행 (옵션 1)
uvicorn main:app --reload

# 또는 (옵션 2)
python main.py
```
> **Note:** main.py에 설정한 포트로 실행하여 모델이 잘 작동하는지 확인하세요.

### Spring Boot 서버 실행 (VSCode)
1. Refresh Gradle
2. 서버 Restart
3. localhost:8080으로 프로토타입(화면) 출력

## 데모 화면
![데모 화면](./images/demo-screenshot.png)

## 성능 테스트
| 입력 길이 | 처리 시간 | 요약 품질 |
|-----------|-----------|-----------|
| 100자     | 0.5초     | 좋음      |
| 300자     | 1.2초     | 양호      |
| 500자     | 2.1초     | 양호      |

## 개발자 정보
- [GitHub 프로필](https://github.com/yourusername)
- 이메일: your.email@example.com
