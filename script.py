from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile, shutil

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

user_data_dir = tempfile.mkdtemp()
options.add_argument(f'--user-data-dir={user_data_dir}')

try:
    driver = webdriver.Chrome(options=options)
except:
    print("get 실행 실패")

try:
    print("🔍 접속 시도 중...")
    driver.get("https://example.com")
    print("✅ 현재 URL:", driver.current_url)

    driver.save_screenshot("screenshot.png")
    print("📸 스크린샷 저장 완료")

finally:
    driver.quit()
    shutil.rmtree(user_data_dir)
