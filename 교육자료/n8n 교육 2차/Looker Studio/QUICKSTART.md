# ⚡ 빠른 시작 - 5분 만에 템플릿 생성하기

## 🎯 목표
Looker Studio에서 AI 트렌드 모니터링 대시보드 템플릿을 자동으로 만들기

## ⏱️ 소요 시간
약 5-10분 (처음 1회만)

---

## 📝 Step 1: 파일 다운로드 및 설치 (2분)

### VSCode 터미널 열기
1. VSCode 실행
2. 상단 메뉴: **Terminal → New Terminal** (또는 Ctrl+`)

### 패키지 설치
터미널에 붙여넣기:
```bash
pip install selenium webdriver-manager
```

---

## 🚀 Step 2: 스크립트 실행 (1분)

### 실행
```bash
python create_looker_template.py
```

### 질문에 답하기
```
시작하시겠습니까? (y/n): y
```

---

## 🔐 Step 3: Google 로그인 (1분)

1. Chrome 브라우저가 자동으로 열림
2. Google 계정으로 로그인
3. Looker Studio 메인 화면 확인
4. 터미널에서 **Enter** 키

---

## 📊 Step 4: 대시보드 만들기 (5-7분)

스크립트가 단계별로 안내합니다:

### 4-1. 데이터 소스 연결
```
✅ Google Sheets 선택
✅ 스프레드시트 검색 또는 URL 입력:
   https://docs.google.com/spreadsheets/d/1VSNMCczgG7j6i0KeWj7JSHOOHt81p0BzSZYSOznHFG4/
✅ "추가" 버튼 클릭
✅ 터미널에서 Enter
```

### 4-2. 보고서 이름 변경
```
✅ 왼쪽 상단 "제목 없는 보고서" 클릭
✅ "AI 트렌드 모니터링 템플릿" 입력
✅ 터미널에서 Enter
```

### 4-3. 필터 4개 추가 (2분)
```
각 필터마다:
1. 상단 "추가" → "컨트롤" → "드롭다운 목록"
2. 필드 선택:
   ① date (날짜 범위)
   ② industry (산업 분야)  
   ③ importance (중요도)
   ④ sentiment (감정)
3. 대시보드 상단에 가로로 배치
4. 터미널에서 Enter
```

### 4-4. 스코어카드 4개 추가 (3분)
```
각 스코어카드마다:
1. 상단 "추가" → "스코어카드"

① 총 건수
   - 측정항목: 레코드 수
   
② 긴급
   - 측정항목: "계산된 필드 만들기"
   - 수식: COUNTIF(is_urgent="TRUE")
   
③ 높은 중요도
   - 측정항목: "계산된 필드 만들기"
   - 수식: COUNTIF(importance="높음")
   
④ 긍정 비율
   - 측정항목: "계산된 필드 만들기"
   - 수식: COUNTIF(sentiment="긍정") / COUNT(timestamp) * 100

2. 가로로 나란히 배치
3. 터미널에서 Enter
```

### 4-5. 파이 차트 추가 (1분)
```
1. 상단 "추가" → "차트" → "파이 차트"
2. 측정기준: sentiment
3. 스타일 탭:
   - 긍정: #70AD47 (초록)
   - 부정: #C00000 (빨강)
   - 중립: #A6A6A6 (회색)
4. 터미널에서 Enter
```

### 4-6. 막대 차트 추가 (1분)
```
1. 상단 "추가" → "차트" → "막대 차트"
2. 측정기준: source
3. 정렬: 내림차순
4. 스타일: 가로 막대
5. 터미널에서 Enter
```

### 4-7. 시계열 차트 추가 (30초)
```
1. 상단 "추가" → "차트" → "시계열 차트"
2. 측정기준: date
3. 가로로 길게 배치
4. 터미널에서 Enter
```

### 4-8. 표 추가 (1분)
```
1. 상단 "추가" → "표"
2. 열 추가:
   - title
   - source
   - importance
   - sentiment
   - url
3. 정렬: timestamp 내림차순
4. 행 수: 10개
5. url 열: 하이퍼링크 활성화
6. 터미널에서 Enter
```

### 4-9. 공유 설정 (30초)
```
1. 오른쪽 상단 "공유" 버튼
2. "링크가 있는 모든 사용자" 선택
3. 권한: "뷰어"
4. 완료
5. 터미널에서 Enter
```

---

## 🎉 Step 5: 완료! (10초)

### 템플릿 ID 확인
터미널에 다음과 같이 표시됩니다:
```
🎉 템플릿 대시보드 생성 완료!
📋 템플릿 ID: abc123xyz456

이 ID를 가이드의 5단계에 넣어주세요!
```

### 템플릿 ID 저장 위치
- 파일: `template_id.txt`
- 내용:
  ```
  TEMPLATE_ID=abc123xyz456
  FULL_URL=https://lookerstudio.google.com/reporting/abc123xyz456
  ```

---

## ✅ 체크리스트

완료했나요?
- [ ] Python 패키지 설치
- [ ] 스크립트 실행
- [ ] Google 로그인
- [ ] 데이터 소스 연결
- [ ] 필터 4개 추가
- [ ] 스코어카드 4개 추가
- [ ] 파이 차트 추가
- [ ] 막대 차트 추가
- [ ] 시계열 차트 추가
- [ ] 표 추가
- [ ] 공유 설정
- [ ] 템플릿 ID 확인

---

## 🔄 다음 단계

1. **템플릿 ID를 복사**하세요
2. **Looker Studio 가이드** 파일을 여세요
3. **5단계**에 템플릿 ID를 붙여넣으세요

이제 모든 사용자가 Python 코드로 **2분 안에** 대시보드를 복제할 수 있습니다! 🚀

---

## 💡 팁

- **한 번만 하면 됩니다!** 템플릿은 재사용됩니다
- **중간에 멈춰도 OK**: 터미널의 안내를 따라 수동 진행
- **나중에 수정 가능**: 템플릿 대시보드는 언제든 편집 가능

---

## ⚠️ 문제 해결

### Chrome이 안 열려요
→ Chrome 설치 확인: https://www.google.com/chrome/

### 로그인이 안 돼요
→ 2단계 인증 필요할 수 있음

### 데이터가 안 보여요
→ Google Sheets URL 다시 확인:
  `https://docs.google.com/spreadsheets/d/1VSNMCczgG7j6i0KeWj7JSHOOHt81p0BzSZYSOznHFG4/`

### 스크립트가 멈췄어요
→ 재실행: `python create_looker_template.py`

---

**완료되면 `template_id.txt`에서 ID를 복사하세요!** 🎊
