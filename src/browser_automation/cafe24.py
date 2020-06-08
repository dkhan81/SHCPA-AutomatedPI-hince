from ..initialization.selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

from ..util.file import *
from ..constants import directory
from ..constants import url
from ..config.access import *


chrome_instance = ChromeWebDriver()
browser = chrome_instance.browser
wait = chrome_instance.wait

browser.get(url.CAFE24_URL)

# 로그인
browser.find_element_by_css_selector("#mall_id").send_keys(ACCESS_INFO['cafe24']['id'])
browser.find_element_by_css_selector("#userpasswd").send_keys(ACCESS_INFO['cafe24']['pw'])
browser.find_element_by_css_selector(".btnSubmit").click()

# 메뉴 진입
browser.find_element_by_css_selector("#QA_Gnb_sales").click()
browser.find_element_by_css_selector("#QA_Lnb_Menu2058").click()

# 기간 설정 및 검색 실행
browser.find_element_by_css_selector("#eBtnSearch").click()
browser.find_element_by_css_selector("#eExcelDownloadBtn").click()

# 새 창으로 전환
browser.switch_to.window(browser.window_handles[1])
browser.find_element_by_css_selector(".excelSubmit").click()

down_req_alert = wait.until(expected_conditions.alert_is_present())
down_req_alert.accept()

# 기존 파일 삭제
delete_file(directory.BROWSER_AUTOMATION_DOWNLOAD, 'cafe24.csv')

# 파일 다운로드
browser.find_element_by_css_selector(".center tr:first-child td:last-child a").click()

# 파일 다운로드 대기
time.sleep(10)

# 파일 다운로드 후 이름 변경
change_latest_filename(directory.BROWSER_AUTOMATION_DOWNLOAD, 'cafe24.csv')

browser.quit()

print('cafe24 완료')
time.sleep(5)