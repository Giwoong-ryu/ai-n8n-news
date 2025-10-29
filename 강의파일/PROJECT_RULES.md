```markdown
# Eazypick File - 개발 규칙

## 🚨 절대 규칙

### 1. 기능 삭제 금지
- 기존 기능 삭제 절대 금지
- ✅ 허용: 개선, 추가, 통합
- ❌ 금지: 제거, 비활성화

### 2. 이모지 사용 금지
- 코드/UI에 이모지(📁✅🔧) 직접 삽입 금지
- PNG 아이콘만 사용: `icons/folder.png`


## 📋 핵심 기능 (삭제 금지)

**file_organizer.py**
- smart_organize_with_preview
- detect_file_patterns
- classify_by_keywords
- execute_smart_normalize
- manage_keywords / manage_keywords_v2
- ActionTracker 통합 (track_action, start_batch, end_batch)

**ui_dashboard_v2.py**
- 대시보드 레이아웃, 미리보기, 되돌리기 UI, 설정 메뉴

**action_tracker.py**
- ActionTracker 클래스, undo_batch, 백업 관리

---

## 🔍 빠른 체크

```python
# check_project.py
import re

files = {
    "file_organizer.py": 2400,
    "ui_dashboard_v2.py": 1800,
    "action_tracker.py": 400
}

emoji_pattern = re.compile(r'[\U0001F300-\U0001F9FF]')

for filename, min_lines in files.items():
    lines = len(open(filename, 'r', encoding='utf-8').readlines())
    print(f"{'✅' if lines >= min_lines else '❌'} {filename}: {lines}줄")
    
    content = open(filename, 'r', encoding='utf-8').read()
    if emoji_pattern.search(content):
        print(f"❌ {filename}에 이모지 발견!")
```

---

## 📝 변경 기록

```markdown
### 2025-XX-XX - [작업명]
- 변경: [파일명] [내용]
- 라인 수: file_organizer(400), ui_dashboard(1400), action_tracker(300)
- 이모지 제거: ✅
- 기능 테스트: ✅
```

---

## 🎯 새 채팅 시작 템플릿

```
[PROJECT_RULES.md 첨부]

현재: file_organizer(400줄), ui_dashboard(1400줄), action_tracker(300줄) 모두 정상

요청: [작업 내용]

제약: 기능 삭제 금지 / 이모지 금지 / 라인 수 유지
```
```

이 정도면 1페이지에 다 보이고, 핵심만 담겨있어서 훨씬 실용적일 거예요! 💪