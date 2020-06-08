from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import os
from ..constants.directory import *

# selenium Chrome 옵션 설정
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_experimental_option('prefs', {
  "download.default_directory": BROWSER_AUTOMATION_DOWNLOAD,
  "directory_upgrade": True
})

# browser 실행
class ChromeWebDriver:
  def __init__(self):
    super().__init__()
    self.browser = webdriver.Chrome(executable_path=os.path.join(INITIALIZATION, "chromedriver"), chrome_options=options)
    self.browser.implicitly_wait(10)
    self.wait = WebDriverWait(self.browser, 30)
