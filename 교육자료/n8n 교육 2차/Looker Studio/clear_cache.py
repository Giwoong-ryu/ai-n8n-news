# -*- coding: utf-8 -*-
import os
import shutil
import sys

def clear_webdriver_cache():
    """WebDriver Manager 캐시 삭제"""
    cache_dir = os.path.expanduser("~/.wdm")

    print("WebDriver Manager 캐시 삭제 중...")
    print(f"캐시 경로: {cache_dir}")

    if os.path.exists(cache_dir):
        try:
            shutil.rmtree(cache_dir)
            print("✅ 캐시 삭제 완료!")
        except Exception as e:
            print(f"❌ 캐시 삭제 실패: {e}")
            return False
    else:
        print("ℹ️  캐시가 없습니다.")

    return True

if __name__ == "__main__":
    if clear_webdriver_cache():
        print("\n이제 스크립트를 다시 실행하세요:")
        print("python create_looker_template.py")
    else:
        print("\n수동으로 다음 폴더를 삭제해주세요:")
        print(os.path.expanduser("~/.wdm"))
