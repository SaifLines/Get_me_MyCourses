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

from filesorg import *

import time 





#THE COURSES DICTIONARY

courses = {"PHIL230 MoralPhilosophy":["Readings", "Slides"],"MATH208 DataScience":["Past Assignments", "Lecture Slides", "Monday Tutorial Materials"],
            "MATH242 Analysis":["Lecture Notes", "Assignmenents (to be submitted on Crowdmark)", "Assignment Solutions"]}  


#SETUP DIRECTORIES

sp = "C:/Users/seifa/Documents/KrayaTest"

setup(courses, sp)







#setup driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\chromeProfiles")
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1200)
driver.get("https://mycourses2.mcgill.ca/d2l/home")


#click on mcgill button
time.sleep(2)
button = driver.find_element_by_id("link1")
button.click()
time.sleep(5)

#ENTER CREDENTIALS + MICROSOFT APP
'''
email = driver.find_element_by_name("loginfmt")
email.send_keys("saif-eddine.abdelkefi@mail.mcgill.ca")
email.send_keys(Keys.RETURN)

time.sleep(5)
password = driver.find_element_by_id("passwordInput")
password.send_keys("XXXXXXXXXXXXXXXXXXXXXXXXX")
password.send_keys(Keys.RETURN)

#waiting to approve on the app
time.sleep(20)

driver.find_element_by_id("idSIButton9").click()

'''


doc = BeautifulSoup(driver.page_source, "html.parser" )
header_mycourses = doc.find(class_="d2l-widget-header")
xpath_header_mycourses = bs4findpath.xpath_soup(header_mycourses)
Sel_mycourses_element = driver.find_element_by_xpath(xpath_header_mycourses)

#click on first course
ac = ActionChains(driver)
ac.move_to_element(Sel_mycourses_element).move_by_offset(-140, 160).context_click().perform()


#WE ARE INSIDE THE COURSE PAGE

time.sleep(1) 
#get the content element from navbar menu 
doc = BeautifulSoup(driver.page_source, "html.parser" )
contentBS = doc.find_all(class_="d2l-navigation-s-link")[1]

contentSL = driver.find_element_by_xpath(bs4findpath.xpath_soup(contentBS))
contentSL.click()



driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
time.sleep(2)
doc = BeautifulSoup(driver.page_source, "html.parser" )


ReadingsBS = doc.find_all(class_="unit")[1]

ReadingsSL= driver.find_element_by_xpath(bs4findpath.xpath_soup(ReadingsBS))

ReadingsSL.click()
time.sleep(1)

#update doc to get the html list of the readings
doc = BeautifulSoup(driver.page_source, "html.parser" )
#print(doc.prettify())
unit_BS = doc.find_all(class_="unit")[1]

children = unit_BS.findChildren("span", recursive=False)[0].find_all(class_="navigation-item")

first_reading_BS = children[0]
first_reading_SL = driver.find_element_by_xpath(bs4findpath.xpath_soup(first_reading_BS))

first_reading_SL.click()


time.sleep(0.5)
doc = BeautifulSoup(driver.page_source, "html.parser" )

downloadButton_BS = doc.find(class_="download-content-button")
downloadButton_SL = driver.find_element_by_xpath(bs4findpath.xpath_soup(downloadButton_BS))

downloadButton_SL.click()


#reswitch to original driver not iframe
#driver.switch_to.default_content()

