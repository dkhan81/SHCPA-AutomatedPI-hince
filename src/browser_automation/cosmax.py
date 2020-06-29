from ..initialization.selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

import time
from datetime import date, timedelta

from ..util.file import *
from ..constants import directory
from ..constants import url
from ..config import access


chrome_instance = ChromeWebDriver()

browser = chrome_instance.browser
wait = chrome_instance.wait

browser.get(url.COSMAX_URL)

browser.find_element_by_css_selector("#userId").send_keys(access.WEB_ACCESS_INFO['cosmax']['id'])
browser.find_element_by_css_selector("#passwd").send_keys(access.WEB_ACCESS_INFO['cosmax']['pw'])
browser.find_element_by_css_selector("#btnLogin").click()

time.sleep(5)

browser.get(url.COSMAX_STOCKLIST_URL)

browser.find_element_by_css_selector("#btnSelect").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#list")))

time.sleep(3)

browser.find_element_by_css_selector("#btnExcel").click()

# 기존 파일 삭제
delete_file(directory.BROWSER_AUTOMATION_DOWNLOAD, 'cosmax.xls')

# 파일 다운로드 대기
time.sleep(10)

# 파일 다운로드 후 이름 변경
change_latest_filename(directory.BROWSER_AUTOMATION_DOWNLOAD, 'cosmax.xls')

browser.quit()






