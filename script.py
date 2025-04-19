from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile, shutil

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

user_data_dir = tempfile.mkdtemp()
options.add_argument(f'--user-data-dir={user_data_dir}')

print("여기까지는 옴")
try:
    browser = webdriver.Chrome(options=options)
    print("브라우저 표시도 성공, 안보일 뿐")
except:
    print("get 실행 실패")
finally:
    shutil.rmtree(user_data_dir)

## 이것조차도 조금 pending이 걸리네. 완전 막히는게 아니고 로딩 개념이구나
