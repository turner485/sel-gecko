import warnings
import time 
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

s=Service('./dependencies/chromedriver.exe')
options = Options()
options.add_argument("window-size=1920,1060")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.headless = True
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://twitch.com/mrrknight")
warnings.filterwarnings("ignore", category=DeprecationWarning) 
act = ActionChains(driver)

print("Initializing twitch watch bot...")

def get_view_count():
    time.sleep(3)
    view_count = driver.find_element_by_class_name("ScAnimatedNumber-sc-1iib0w9-0").text
    sys.stdout.write("\r")
    sys.stdout.write(f"Current View Count: {view_count}")
    sys.stdout.flush()
    return view_count
###

while True:
    get_view_count()


