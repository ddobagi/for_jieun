from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile
import shutil

# Headless 설정
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# ✅ 임시 user-data-dir 경로 생성 (고유하게)
user_data_dir = tempfile.mkdtemp()
options.add_argument(f'--user-data-dir={user_data_dir}')

# 크롬 드라이버 실행
browser = webdriver.Chrome(options=options)

URL = "https://edumaidenvoyage.com/wp_mock/dispWp_mockSessionDetail?session_srl=78414"


try:
    browser.get(URL)
    print("✅ 현재 URL:", browser.current_url)


    flag = True

    xpath = "//*[contains(@class, 'payment-btn') and contains(@class, 'btn')]"
    code = "checkmate25"

    while flag:
        url_list = browser.current_url
        print(url_list)
        try:
            element = browser.find_element(By.XPATH, xpath)
            print(f"XPATH '{xpath}'를 가진 요소가 존재합니다.")


            browser.execute_script("""
                var input = document.createElement('input');
                input.type = 'text';
                input.id = 'selenium-input';
                input.placeholder = '여기에 값을 입력하세요';
                input.style.position = 'fixed';
                input.style.top = '100px';
                input.style.left = '100px';
                input.style.zIndex = 9999;
                input.style.fontSize = '20px';
                document.body.appendChild(input);
            """)
            
            
            print("[브라우저에 입력창을 생성했습니다. 값을 입력한 후 15초를 기다립니다.]")
            time.sleep(15)  # 사용자가 브라우저에서 입력할 시간을 줍니다

            # 2. 사용자가 입력한 값을 가져오기
            value = browser.execute_script("return document.getElementById('selenium-input').value;")
            print("입력된 값:", value)

            if value == code:
                flag = False
                element.click()
            else:
                print("code가 일치하지 않습니다")
        except:
            print(f'현재 페이지에는 {xpath}를 가진 요소가 존재하지 않습니다')
        else:
            print(code)
        finally:
            time.sleep(5)

finally:
    browser.quit()
    shutil.rmtree(user_data_dir)  # 🧼 임시 디렉토리 깔끔하게 삭제




