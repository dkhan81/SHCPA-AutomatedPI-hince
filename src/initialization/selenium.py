from selenium import webdriver
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
def makeNewBrowser():
  browser = webdriver.Chrome(executable_path=os.path.join(INITIALIZATION, "chromedriver"), chrome_options=options)
  browser.implicitly_wait(10)

  return browser