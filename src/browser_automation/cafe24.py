from ..initialization.selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

from ..util.util import *
from ..constants.directory import *
from ..config.access import *


browser = makeNewBrowser()
browser.get('https://eclogin.cafe24.com/Shop/')

wait = WebDriverWait(browser, 30)

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
deleteFile(BROWSER_AUTOMATION_DOWNLOAD, 'cafe24.csv')

# 파일 다운로드
browser.find_element_by_css_selector(".center tr:first-child td:last-child a").click()

# 파일 다운로드 대기
time.sleep(8)

# 파일 다운로드 후 이름 변경
changeLatestFileName(BROWSER_AUTOMATION_DOWNLOAD, 'cafe24.csv')

browser.quit()

print('cafe24 완료')
time.sleep(5)