from ..initialization.selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

from ..util.util import *
from ..constants.directory import *
from ..config.access import *


browser = makeNewBrowser()
browser.get('https://pin.wconcept.co.kr/')

wait = WebDriverWait(browser, 30)

# original window 저장
original_window = browser.current_window_handle

# 로그인
browser.find_element_by_css_selector("#userid").send_keys('vivawave')
browser.find_element_by_css_selector("#pw").send_keys('vivahince4040!')
browser.find_element_by_css_selector(".login-form__button").click()

# 팝업창 뜰 때까지 기다리기
time.sleep(5)

# 팝업창이 뜨는 경우 모두 닫기
if(len(browser.window_handles) > 1):
  for window_handle in browser.window_handles:
    if window_handle != original_window:
        browser.switch_to.window(window_handle)
        browser.close()


browser.switch_to.window(browser.window_handles[0])
browser.get("https://newpin.wconcept.co.kr/Order/ShippingOrderComplete")

# 날짜 지정

# 조회 버튼 클릭
browser.find_element_by_css_selector(".row:last-child .dropdown:last-child").click()
browser.find_element_by_css_selector(".row:last-child .dropdown:last-child .item:nth-child(2)").click()
browser.find_element_by_css_selector("button[id='btnSearch']").click()
browser.find_element_by_css_selector("button[name='btnExcel']").click()

# alert창 확인
down_req_alert = wait.until(expected_conditions.alert_is_present())
down_req_alert.accept()

# 기존 파일 삭제
deleteFile(BROWSER_AUTOMATION_DOWNLOAD, 'wconcept.xlsx')

# 파일 다운로드 대기
time.sleep(8)

# 파일 다운로드 후 이름 변경
changeLatestFileName(BROWSER_AUTOMATION_DOWNLOAD, 'wconcept.xlsx')

browser.quit()

