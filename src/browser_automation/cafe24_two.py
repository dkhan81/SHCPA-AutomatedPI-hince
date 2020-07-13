from ..initialization.selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
import time

from ..util import file
from ..util import time as timeutil
from ..constants import directory
from ..constants import url
from ..config import access


chrome_instance = ChromeWebDriver()
browser = chrome_instance.browser
wait = chrome_instance.wait

browser.get(url.CAFE24_URL)

# 로그인
browser.find_element_by_css_selector("#mall_id").send_keys(access.WEB_ACCESS_INFO['cafe24']['id'])
browser.find_element_by_css_selector("#userpasswd").send_keys(access.WEB_ACCESS_INFO['cafe24']['pw'])
browser.find_element_by_css_selector(".btnSubmit").click()

# 메뉴 진입
browser.find_element_by_css_selector("#QA_Gnb_sales").click()
browser.find_element_by_css_selector("#QA_Lnb_Menu74").click()

# 기간 설정 및 검색 실행
browser.execute_script("document.getElementById('startDate').value = " + timeutil.get_past_date(20, with_hyphen=True))
browser.find_element_by_css_selector(".btnDate:nth-child(4)").click()
browser.find_element_by_css_selector("#eBtnSearch").click()
browser.find_element_by_css_selector("#eExcelDownloadBtn").click()

# 새 창으로 전환
browser.switch_to.window(browser.window_handles[1])

# Select Box에서 선택
Select(browser.find_element_by_css_selector("#aManagesList")).select_by_visible_text("삼화회계법인테스트")

browser.find_element_by_css_selector(".excelSubmit").click()

down_req_alert = wait.until(expected_conditions.alert_is_present())
down_req_alert.accept()

# 기존 파일 삭제
# file.delete_file(directory.BROWSER_AUTOMATION_DOWNLOAD, 'cafe24.csv')

# 파일 다운로드
browser.find_element_by_css_selector(".center tr:first-child td:last-child a").click()

# 파일 다운로드 대기
time.sleep(10)

# 파일 다운로드 후 이름 변경
file.change_latest_filename(directory.BROWSER_AUTOMATION_DOWNLOAD, 'cafe24_two.csv')

browser.quit()

print('cafe24 완료')
time.sleep(5)