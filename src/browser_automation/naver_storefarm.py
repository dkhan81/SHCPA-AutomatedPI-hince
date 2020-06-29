from ..initialization.selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

from ..util.file import *
from ..constants import directory
from ..constants import url
from ..config import access


chrome_instance = ChromeWebDriver()
browser = chrome_instance.browser
wait = chrome_instance.wait

browser.get(url.NAVER_STOREFARM_URL)

# 로그인
browser.find_element_by_css_selector("#loginId").send_keys(access.WEB_ACCESS_INFO['naver_storefarm']['id'])
browser.find_element_by_css_selector("#loginPassword").send_keys(access.WEB_ACCESS_INFO['naver_storefarm']['pw'])
browser.find_element_by_css_selector("#loginButton").click()

time.sleep(7)

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".modal-content .close")))
browser.find_element_by_css_selector('.modal-content .close').click()

# 날짜 지정

# 조회 버튼 클릭
browser.find_element_by_css_selector("ul[role='menu'] > li:nth-child(2)").click()
browser.find_element_by_css_selector("ul[role='menu'] > li:nth-child(2) >ul > li:nth-child(5)").click()

time.sleep(7)
wait.until(expected_conditions.frame_to_be_available_and_switch_to_it('__naverpay'))

# Select Box에서 선택
Select(browser.find_element_by_css_selector(".npay_board_table select")).select_by_visible_text("배송완료일")
browser.find_element_by_css_selector("option[value='DELIVERY_COMPLETED']").click()
browser.find_element_by_css_selector(".button_area > button").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "td[data-column-name='orderStatus']")))
browser.find_element_by_css_selector(".right_area button:nth-child(4)").click()

# 기존 파일 삭제
delete_file(directory.BROWSER_AUTOMATION_DOWNLOAD, 'naver_storefarm.xlsx')

# 파일 다운로드 대기
time.sleep(10)

# 파일 다운로드 후 이름 변경
change_latest_filename(directory.BROWSER_AUTOMATION_DOWNLOAD, 'naver_storefarm.xlsx')

browser.quit()

