from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains


from bs4 import BeautifulSoup
import bs4findpath

import time 

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\chromeProfiles")
options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)




driver.set_window_position(0, 0)
driver.set_window_size(1920, 1200)
driver.get("https://mycourses2.mcgill.ca/d2l/home")



time.sleep(2)

button = driver.find_element_by_id("link1")
button.click()
time.sleep(5)

print("elemment is")
print(button)

