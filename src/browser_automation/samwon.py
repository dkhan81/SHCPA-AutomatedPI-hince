from ..initialization.selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from datetime import date, timedelta

from ..util.file import *
from ..constants import directory
from ..constants import url
from ..config import access


chrome_instance = ChromeWebDriver()

browser = chrome_instance.browser
wait = chrome_instance.wait

browser.get(url.SAMWON_URL)

browser.find_element_by_css_selector("input[name='id']").send_keys(access.WEB_ACCESS_INFO['samwon']['id'])
browser.find_element_by_css_selector("input[name='pw']").send_keys(access.WEB_ACCESS_INFO['samwon']['pw'])
browser.find_element_by_css_selector("input[type='button']").click()

browser.find_element_by_css_selector("a:nth-child(4)").click()

todayDate = date.today()
yesterdayDate = str(todayDate - timedelta(days=1))

browser.find_element_by_css_selector("input[name='dat2']").send_keys(yesterdayDate)
browser.find_element_by_css_selector("td > input[type='button']").click()
browser.find_element_by_css_selector("table:nth-child(2) a").click()

# 기존 파일 삭제
delete_file(directory.BROWSER_AUTOMATION_DOWNLOAD, 'samwon.xls')

# 파일 다운로드 대기
time.sleep(10)

# 파일 다운로드 후 이름 변경
change_latest_filename(directory.BROWSER_AUTOMATION_DOWNLOAD, 'samwon.xls')

browser.quit()






