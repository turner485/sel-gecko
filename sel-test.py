from selenium import webdriver
import threading
import warnings
import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions


warnings.filterwarnings("ignore", category=DeprecationWarning) 
def test_logic():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.binary_location = ('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    driver = webdriver.Firefox(options=options, firefox_profile=profile)
    url = 'https://www.twitch.tv/revolu7ion'
    driver.get(url)

    time.sleep(15)
    elem = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/main/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div[4]/div/div[3]')
    elem.click()

    time.sleep(10)
    driver.quit()

N = 5   # Number of browsers to spawn
thread_list = list()

# Start test
for i in range(N):
    t = threading.Thread(name='Test {}'.format(i), target=test_logic)
    t.start()
    time.sleep(1)
    print(t.name + ' started!')
    thread_list.append(t)

# Wait for all threads to complete
for thread in thread_list:
    thread.join()

print('Test completed!')