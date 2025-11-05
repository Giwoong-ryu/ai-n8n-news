# 🚀 Looker Studio 템플릿 자동 생성 도구

이 도구는 AI 트렌드 모니터링 대시보드 템플릿을 Looker Studio에서 자동으로 생성합니다.

## 📋 준비사항

1. ✅ Python 3.8 이상
2. ✅ Chrome 브라우저
3. ✅ Google 계정
4. ✅ VSCode (선택사항)

## 🔧 설치 방법

### 1단계: 파일 다운로드
- `create_looker_template.py`
- `requirements.txt`

### 2단계: 필수 패키지 설치

터미널(또는 VSCode 터미널)에서 다음 명령어 실행:

```bash
pip install -r requirements.txt
```

또는 개별 설치:

```bash
pip install selenium webdriver-manager
```

## 🎯 사용 방법

### 실행

터미널에서:

```bash
python create_looker_template.py
```

또는 VSCode에서:
1. `create_looker_template.py` 파일 열기
2. F5 키 누르기 (또는 상단 메뉴 → 실행 → 디버깅 시작)

### 프로세스

스크립트가 자동으로 Chrome 브라우저를 열고 안내합니다:

1. **Google 로그인** (수동)
   - 브라우저가 열리면 Google 계정으로 로그인
   - 로그인 완료 후 터미널에서 Enter

2. **데이터 소스 연결** (반자동)
   - Google Sheets 커넥터 선택
   - 스프레드시트 검색 또는 URL 입력
   - 완료 후 Enter

3. **차트 추가** (수동 - 안내 따라하기)
   - 필터 4개 (날짜, 산업, 중요도, 감정)
   - 스코어카드 4개
   - 파이 차트
   - 막대 차트
   - 시계열 차트
   - 표

4. **완료!**
   - 템플릿 ID가 자동으로 추출됨
   - `template_id.txt` 파일에 저장됨

## 📊 생성되는 대시보드 구성

```
┌─────────────────────────────────────────────────┐
│ [날짜] [산업] [중요도] [감정] ← 필터 4개        │
├─────────────────────────────────────────────────┤
│ [총건수] [긴급] [높은중요도] [긍정비율]         │
├───────────────────┬─────────────────────────────┤
│   감정 분석       │      출처별 뉴스            │
│   (파이 차트)     │      (막대 차트)            │
├───────────────────┴─────────────────────────────┤
│           일별 트렌드 (시계열)                  │
├─────────────────────────────────────────────────┤
│         최신 뉴스 TOP 10 (표)                   │
└─────────────────────────────────────────────────┘
```

## 📝 출력 파일

- `template_id.txt`: 생성된 템플릿 ID

## ❓ FAQ

### Q1. 로그인이 안 돼요!
A: 2단계 인증이 활성화된 계정은 추가 인증이 필요합니다.

### Q2. Chrome이 자동으로 안 열려요!
A: Chrome이 설치되어 있는지 확인하세요. 또는 수동으로 실행:
   1. Chrome에서 https://lookerstudio.google.com/ 열기
   2. 스크립트의 안내를 따라 수동 진행

### Q3. 데이터 소스 연결이 안 돼요!
A: Google Sheets URL을 직접 입력하세요:
   `https://docs.google.com/spreadsheets/d/1VSNMCczgG7j6i0KeWj7JSHOOHt81p0BzSZYSOznHFG4/edit`

### Q4. 중간에 멈췄어요!
A: 괜찮습니다! 터미널의 안내를 따라 수동으로 진행하면 됩니다.
   각 단계마다 명확한 안내가 표시됩니다.

## 🎉 완료 후

1. `template_id.txt` 파일 열기
2. 템플릿 ID 복사
3. Looker Studio 가이드의 5단계에 붙여넣기

템플릿 URL 예시:
```
https://lookerstudio.google.com/reporting/[YOUR_TEMPLATE_ID]
```

## 💡 팁

- 처음 실행 시 10-15분 정도 소요됩니다
- 차트 배치는 나중에 수정 가능합니다
- 템플릿 생성은 **딱 1번만** 하면 됩니다!
- 이후 모든 사용자는 Python 코드로 2분 안에 복제 가능

## 🐛 문제 발생 시

1. 스크립트 재실행: `python create_looker_template.py`
2. Chrome 재시작
3. 로그아웃 후 다시 로그인

## 📞 지원

문제가 계속되면:
1. 터미널의 오류 메시지 확인
2. Chrome 버전 확인 (최신 버전 권장)
3. Python 버전 확인: `python --version`

---

Made with ❤️ for AI Trend Monitoring
