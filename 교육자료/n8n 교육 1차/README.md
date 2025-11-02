# -# AI 뉴스 자동화 워크플로우 교육 1차

n8n을 활용한 AI 뉴스 자동 요약 및 카카오톡 전송 워크플로우 교육 자료입니다.

## 📚 교육 자료

### 1. 강의 자료
- [n8n 교육자료 _ 크롤링부터 카톡전송 까지.xlsx] - 전체 워크플로우 가이드

### 2. 워크플로우 구조
```
RSS Read → Limit → Code → Gemini → Kakao
```

### 3. 필요한 준비물
- n8n 설치 (Docker 또는 Self-hosted)
- Google Gemini API 키
- 카카오 디벨로퍼스 앱 등록

### 4. 주요 기능
- ✅ RSS 피드 자동 수집
- ✅ AI(Gemini)로 10개 중 3개 선별 + 요약
- ✅ 카카오톡 자동 전송
- ✅ 완전 무료 운영

## 🚀 빠른 시작

1. [강의자료 다운로드](./n8n 교육자료 _ 크롤링부터 카톡전송 까지.xlsx)
2. Gemini API 키 발급: https://aistudio.google.com/app/apikey
3. 워크플로우 따라 만들기

## 📞 문의
- 이메일: your-email@example.com
- 블로그: https://your-blog.com

## 📝 라이선스
MIT License - 자유롭게 사용하세요!
```

### 4단계: 교육생에게 링크 공유
```
https://github.com/유저명/n8n-ai-news-workshop
```

## 방법 2: 폴더 구조화 (더 전문적)
```
n8n-ai-news-workshop/
├── README.md                    # 메인 설명
├── docs/
│   └── AI뉴스_워크플로우_강의자료.xlsx
├── workflows/
│   └── ai-news-workflow.json    # n8n JSON export
├── images/
│   ├── workflow-overview.png
│   ├── gemini-setup.png
│   └── kakao-setup.png
├── code-samples/
│   ├── code-node-1.js
│   └── code-node-2.js
└── LICENSE
