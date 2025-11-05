# -*- coding: utf-8 -*-
"""
Looker Studio 템플릿 대시보드 자동 생성 스크립트

이 스크립트는 Selenium을 사용하여 Looker Studio에서
AI 트렌드 모니터링 대시보드 템플릿을 자동으로 생성합니다.

요구사항:
- Python 3.8+
- Chrome 브라우저
- selenium, webdriver-manager 설치

설치 방법:
pip install selenium webdriver-manager

사용 방법:
python create_looker_template.py
"""

import sys
import io

# Windows 환경에서 UTF-8 출력 설정
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

# Google Sheets 정보
SPREADSHEET_ID = "1VSNMCczgG7j6i0KeWj7JSHOOHt81p0BzSZYSOznHFG4"
WORKSHEET_ID = "0"  # 첫 번째 시트

class LookerStudioAutomation:
    def __init__(self):
        """Selenium WebDriver 초기화"""
        print("🚀 Looker Studio 자동화 시작...")

        # Chrome 옵션 설정
        chrome_options = Options()
        # chrome_options.add_argument('--headless')  # 백그라운드 실행 (주석 처리하면 브라우저 보임)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--start-maximized')

        # WebDriver 초기화 (Selenium 4의 자동 관리 사용)
        try:
            print("Chrome 브라우저 연결 중...")
            print("(처음 실행 시 ChromeDriver를 자동으로 다운로드합니다)")

            # Selenium 4는 자동으로 ChromeDriver를 관리합니다
            self.driver = webdriver.Chrome(options=chrome_options)
            self.wait = WebDriverWait(self.driver, 20)
            print("✅ Chrome 브라우저 연결 완료!")
        except Exception as e:
            print(f"❌ Chrome 브라우저 연결 실패: {e}")
            print("\n해결 방법:")
            print("1. Chrome 브라우저가 설치되어 있는지 확인")
            print("2. Chrome을 최신 버전으로 업데이트")
            print("3. 관리자 권한으로 실행")
            print("\n또는 다음을 시도해보세요:")
            print("- Chrome 브라우저 재설치")
            print("- 바이러스 백신 프로그램이 차단하는지 확인")
            raise
        
    def login_google(self):
        """Google 계정 로그인 (수동)"""
        print("\n📝 Google 로그인이 필요합니다.")
        print("브라우저가 열리면 로그인해주세요...")
        
        # Looker Studio 메인 페이지로 이동
        self.driver.get("https://lookerstudio.google.com/")
        
        print("\n⏳ 로그인을 완료하고 Looker Studio 메인 화면이 나올 때까지 기다려주세요...")
        print("로그인 완료 후 Enter를 눌러주세요...")
        input()
        
    def create_new_report(self):
        """새 보고서 생성"""
        print("\n📊 새 보고서 생성 중...")
        
        try:
            # "만들기" 버튼 클릭
            create_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., '만들기') or contains(., 'Create')]"))
            )
            create_button.click()
            time.sleep(2)
            
            # "보고서" 선택
            report_option = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(., '보고서') or contains(., 'Report')]"))
            )
            report_option.click()
            time.sleep(3)
            
            print("✅ 새 보고서 생성 완료!")
            
        except Exception as e:
            print(f"❌ 보고서 생성 실패: {e}")
            print("\n수동으로 진행해주세요:")
            print("1. '만들기' 버튼 클릭")
            print("2. '보고서' 선택")
            print("3. Enter를 눌러 계속...")
            input()
    
    def connect_data_source(self):
        """Google Sheets 데이터 소스 연결"""
        print("\n🔗 데이터 소스 연결 중...")
        
        try:
            # Google Sheets 커넥터 찾기
            sheets_connector = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Google Sheets') or contains(., 'Google 스프레드시트')]"))
            )
            sheets_connector.click()
            time.sleep(2)
            
            # 스프레드시트 검색 또는 URL 입력
            print(f"\n📋 스프레드시트 ID: {SPREADSHEET_ID}")
            print("브라우저에서 해당 스프레드시트를 선택해주세요...")
            print("선택 완료 후 Enter를 눌러주세요...")
            input()
            
            print("✅ 데이터 소스 연결 완료!")
            
        except Exception as e:
            print(f"❌ 데이터 소스 연결 실패: {e}")
            print("\n수동으로 진행해주세요:")
            print("1. 'Google Sheets' 커넥터 선택")
            print("2. 스프레드시트 선택")
            print("3. '추가' 버튼 클릭")
            print("4. Enter를 눌러 계속...")
            input()
    
    def add_filters(self):
        """필터 4개 추가 (날짜, 산업, 중요도, 감정)"""
        print("\n🎯 필터 추가 중...")
        
        filters = [
            ("date", "날짜 범위"),
            ("industry", "산업 분야"),
            ("importance", "중요도"),
            ("sentiment", "감정")
        ]
        
        print("\n수동으로 필터를 추가해주세요:")
        for field, label in filters:
            print(f"  - {label} ({field})")
        
        print("\n방법:")
        print("1. 상단 메뉴 '추가' → '컨트롤' → '드롭다운 목록' 선택")
        print("2. 위 4개 필드를 각각 추가")
        print("3. 필터를 대시보드 상단에 가로로 배치")
        print("\n완료 후 Enter를 눌러주세요...")
        input()
        
        print("✅ 필터 추가 완료!")
    
    def add_scorecards(self):
        """스코어카드 4개 추가"""
        print("\n📊 스코어카드 4개 추가 중...")
        
        scorecards = [
            {
                "label": "총 건수",
                "metric": "레코드 수",
                "formula": None
            },
            {
                "label": "긴급",
                "metric": "긴급 건수",
                "formula": 'COUNTIF(is_urgent="TRUE")'
            },
            {
                "label": "높은 중요도",
                "metric": "높은 중요도",
                "formula": 'COUNTIF(importance="높음")'
            },
            {
                "label": "긍정 비율",
                "metric": "긍정 비율",
                "formula": 'COUNTIF(sentiment="긍정") / COUNT(timestamp) * 100'
            }
        ]
        
        print("\n수동으로 스코어카드를 추가해주세요:")
        for i, card in enumerate(scorecards, 1):
            print(f"\n{i}. {card['label']}")
            print(f"   - 상단 메뉴 '추가' → '스코어카드' 선택")
            if card['formula']:
                print(f"   - 측정항목: '계산된 필드 만들기' → 수식 입력: {card['formula']}")
            else:
                print(f"   - 측정항목: {card['metric']} (기본값)")
            print(f"   - 라벨: {card['label']}")
        
        print("\n4개를 가로로 나란히 배치해주세요.")
        print("\n완료 후 Enter를 눌러주세요...")
        input()
        
        print("✅ 스코어카드 추가 완료!")
    
    def add_pie_chart(self):
        """파이 차트 추가 (감정 분석)"""
        print("\n🥧 파이 차트 추가 중...")
        
        print("\n수동으로 파이 차트를 추가해주세요:")
        print("1. 상단 메뉴 '추가' → '차트' → '파이 차트' 선택")
        print("2. 설정:")
        print("   - 측정기준: sentiment")
        print("   - 측정항목: 레코드 수")
        print("3. 스타일:")
        print("   - 긍정: 초록색 (#70AD47)")
        print("   - 부정: 빨간색 (#C00000)")
        print("   - 중립: 회색 (#A6A6A6)")
        print("4. 스코어카드 아래 왼쪽에 배치")
        
        print("\n완료 후 Enter를 눌러주세요...")
        input()
        
        print("✅ 파이 차트 추가 완료!")
    
    def add_bar_chart(self):
        """막대 차트 추가 (출처별)"""
        print("\n📊 막대 차트 추가 중...")
        
        print("\n수동으로 막대 차트를 추가해주세요:")
        print("1. 상단 메뉴 '추가' → '차트' → '막대 차트' 선택")
        print("2. 설정:")
        print("   - 측정기준: source")
        print("   - 측정항목: 레코드 수")
        print("   - 정렬: 내림차순")
        print("3. 스타일:")
        print("   - 막대 방향: 가로")
        print("4. 파이 차트 오른쪽에 배치")
        
        print("\n완료 후 Enter를 눌러주세요...")
        input()
        
        print("✅ 막대 차트 추가 완료!")
    
    def add_time_series(self):
        """시계열 차트 추가"""
        print("\n📈 시계열 차트 추가 중...")
        
        print("\n수동으로 시계열 차트를 추가해주세요:")
        print("1. 상단 메뉴 '추가' → '차트' → '시계열 차트' 선택")
        print("2. 설정:")
        print("   - 측정기준: date")
        print("   - 측정항목: 레코드 수")
        print("3. 막대 차트 아래에 가로로 길게 배치")
        
        print("\n완료 후 Enter를 눌러주세요...")
        input()
        
        print("✅ 시계열 차트 추가 완료!")
    
    def add_table(self):
        """표 추가 (최신 뉴스 TOP 10)"""
        print("\n📋 표 추가 중...")
        
        print("\n수동으로 표를 추가해주세요:")
        print("1. 상단 메뉴 '추가' → '표' 선택")
        print("2. 열 추가:")
        print("   - title (제목)")
        print("   - source (출처)")
        print("   - importance (중요도)")
        print("   - sentiment (감정)")
        print("   - url (링크)")
        print("3. 정렬: timestamp 내림차순")
        print("4. 표시 행 수: 10개")
        print("5. URL 열: 하이퍼링크 활성화")
        print("6. 시계열 차트 아래에 가로로 길게 배치")
        
        print("\n완료 후 Enter를 눌러주세요...")
        input()
        
        print("✅ 표 추가 완료!")
    
    def set_report_name(self):
        """보고서 이름 설정"""
        print("\n📝 보고서 이름 설정 중...")
        
        print("\n보고서 이름을 다음으로 변경해주세요:")
        print("'AI 트렌드 모니터링 템플릿'")
        print("\n방법:")
        print("1. 왼쪽 상단 '제목 없는 보고서' 클릭")
        print("2. 'AI 트렌드 모니터링 템플릿' 입력")
        
        print("\n완료 후 Enter를 눌러주세요...")
        input()
        
        print("✅ 보고서 이름 설정 완료!")
    
    def get_template_id(self):
        """템플릿 ID 가져오기"""
        print("\n🔑 템플릿 ID 가져오는 중...")
        
        try:
            current_url = self.driver.current_url
            print(f"\n현재 URL: {current_url}")
            
            # URL에서 reportId 추출
            if "/reporting/" in current_url:
                template_id = current_url.split("/reporting/")[1].split("/")[0].split("?")[0]
                print(f"\n✅ 템플릿 ID: {template_id}")
                
                # 파일로 저장
                with open("/home/claude/template_id.txt", "w") as f:
                    f.write(f"TEMPLATE_ID={template_id}\n")
                    f.write(f"FULL_URL={current_url}\n")
                
                print(f"\n✅ 템플릿 ID가 저장되었습니다: /home/claude/template_id.txt")
                
                return template_id
            else:
                print("❌ URL에서 템플릿 ID를 찾을 수 없습니다.")
                print("수동으로 URL을 확인해주세요.")
                return None
                
        except Exception as e:
            print(f"❌ 템플릿 ID 추출 실패: {e}")
            return None
    
    def share_settings(self):
        """공유 설정"""
        print("\n🔗 공유 설정 중...")
        
        print("\n수동으로 공유 설정을 해주세요:")
        print("1. 오른쪽 상단 '공유' 버튼 클릭")
        print("2. '링크가 있는 모든 사용자' 선택")
        print("3. 권한: '뷰어' 선택")
        print("4. '완료' 클릭")
        
        print("\n완료 후 Enter를 눌러주세요...")
        input()
        
        print("✅ 공유 설정 완료!")
    
    def run(self):
        """전체 프로세스 실행"""
        try:
            # 1. Google 로그인
            self.login_google()
            
            # 2. 새 보고서 생성
            self.create_new_report()
            
            # 3. 데이터 소스 연결
            self.connect_data_source()
            
            # 4. 보고서 이름 설정
            self.set_report_name()
            
            # 5. 필터 추가
            self.add_filters()
            
            # 6. 스코어카드 추가
            self.add_scorecards()
            
            # 7. 파이 차트 추가
            self.add_pie_chart()
            
            # 8. 막대 차트 추가
            self.add_bar_chart()
            
            # 9. 시계열 차트 추가
            self.add_time_series()
            
            # 10. 표 추가
            self.add_table()
            
            # 11. 공유 설정
            self.share_settings()
            
            # 12. 템플릿 ID 가져오기
            template_id = self.get_template_id()
            
            if template_id:
                print("\n" + "="*60)
                print("🎉 템플릿 대시보드 생성 완료!")
                print("="*60)
                print(f"\n📋 템플릿 ID: {template_id}")
                print(f"\n이 ID를 가이드의 5단계에 넣어주세요!")
                print("\n템플릿 URL:")
                print(f"https://lookerstudio.google.com/reporting/{template_id}")
                print("\n" + "="*60)
            
            print("\n브라우저를 닫으려면 Enter를 눌러주세요...")
            input()
            
        except Exception as e:
            print(f"\n❌ 오류 발생: {e}")
            print("\n브라우저를 수동으로 확인해주세요.")
            input()
        
        finally:
            self.driver.quit()
            print("\n✅ 프로그램 종료")


if __name__ == "__main__":
    print("="*60)
    print("🚀 Looker Studio 템플릿 자동 생성 도구")
    print("="*60)
    print("\n이 스크립트는 Looker Studio 템플릿 대시보드를 생성합니다.")
    print("\n준비사항:")
    print("  ✅ Chrome 브라우저")
    print("  ✅ Google 계정")
    print("  ✅ 인터넷 연결")
    print("\n시작하시겠습니까? (y/n): ", end="")
    
    if input().lower() != 'y':
        print("프로그램을 종료합니다.")
        sys.exit(0)
    
    automation = LookerStudioAutomation()
    automation.run()
