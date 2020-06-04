import os
import sys

ROOT_PATH = os.path.dirname(sys.modules['__main__'].__file__)

BROWSER_AUTOMATION =  os.path.abspath(ROOT_PATH + "/browser_automation")
BROWSER_AUTOMATION_DOWNLOAD = os.path.abspath(ROOT_PATH + "/browser_automation/download")
CONSTANTS = os.path.abspath(ROOT_PATH + "/constants")
INITIALIZATION = os.path.abspath(ROOT_PATH + "/initialization")