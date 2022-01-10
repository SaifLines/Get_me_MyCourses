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

courses = {
"MATH208 DataScience":["Lecture Slides", "Monday Tutorial Materials"]
            }  


#SETUP DIRECTORIES

sp = "C:/Users/seifa/Documents/KrayaTest"






#DRIVER SETUP

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\chromeProfiles")
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1200)

def goto_main():
    #mcgill page
    driver.get("https://mycourses2.mcgill.ca/d2l/home")
    
    #click on mcgill button
    try:
        button = WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.ID, "link1"))
        )
        button.click()
        
    except:
        pass
    



def from_main_to_course(x,y):
    print()
    print(f"positions are {x} and {y}")
    #click on course card
    doc = BeautifulSoup(driver.page_source, "html.parser" )
    header_mycourses = doc.find(class_="d2l-widget-header")
    xpath_header_mycourses = bs4findpath.xpath_soup(header_mycourses)
    Sel_mycourses_element = driver.find_element_by_xpath(xpath_header_mycourses)

    #click on first course
    ac = ActionChains(driver)
    ac.move_to_element(Sel_mycourses_element).move_by_offset(x,y).click().perform()
    
    

    

def update_course(position, courses):
    if position==1:
        from_main_to_course(-140,160)
    elif position == 2:
        from_main_to_course(130,160)
    elif position == 3:
        from_main_to_course(-140,480)
    elif position == 4:
        from_main_to_course(130,480)

    time.sleep(1)
    #get the course key
    the_course=""
    i=0
    for course in courses:
        if i+1 != position:
            i = i+1
            continue
        if i+1== position:
            the_course = course
            break
    
    #to be deleted
    the_course = "MATH208 DataScience"
    
    # Click on content
    doc = BeautifulSoup(driver.page_source, "html.parser" )
    contentBS = doc.find_all(class_="d2l-navigation-s-link")[1]

    contentSL = driver.find_element_by_xpath(bs4findpath.xpath_soup(contentBS))
    contentSL.click()
    time.sleep(0.5)
    doc = BeautifulSoup(driver.page_source, "html.parser" )

    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    time.sleep(2)
    doc = BeautifulSoup(driver.page_source, "html.parser" )

    
    for rubrique in courses[the_course]:
        
        all_sections = doc.find_all(class_="unit")
        i=0
        for section in all_sections:
            section_found = section.find(text=rubrique)
            if section_found == None:
                i = i+1
                continue
            else:
                
                section_found_SL = driver.find_element_by_xpath(bs4findpath.xpath_soup(section_found))
                section_found_SL.click()
                time.sleep(0.5)
                doc = BeautifulSoup(driver.page_source, "html.parser" )
                
                

                section_found_BS2 =  doc.find_all(class_="unit")[i]

                children = section_found_BS2.findChildren("span", recursive=False)[0].find_all(class_="navigation-item")

                for child in children:
                    child_SL = driver.find_element_by_xpath(bs4findpath.xpath_soup(child))
                    child_SL.click()

                    time.sleep(0.5)
                    doc = BeautifulSoup(driver.page_source, "html.parser" )

                    downloadButton_BS = doc.find(class_="download-content-button")
                    downloadButton_SL = driver.find_element_by_xpath(bs4findpath.xpath_soup(downloadButton_BS))

                    try:
                        downloadButton_SL.click()
                        time.sleep(1.2)
                    except:
                        print("exceptionnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
                        time.sleep(10)
                        #on very rare occasions the file will be an html and cannot be downloaded
                        
                    
                    try:
                        f = locateLastFile()
                        moveFile(the_course, rubrique, f, "C:/Users/seifa/Documents/KrayaTest")
                    except:
                        print(f"EXCEPTION CAUGHT MADAFAKAAAAAAA   file: {(f.split('/'))[-1]}")
                        time.sleep(1)
                        f = locateLastFile()
                        moveFile(the_course, rubrique, f, "C:/Users/seifa/Documents/KrayaTest")
                break


        time.sleep(5)
                




        #download all that subdirectory files


    #reswitch to original driver not iframe
    driver.switch_to.default_content()
        #go to the course webpage again from main   

    #go to main from course for the other courses
    goto_main()


def update_courses(positions, courses):
    
    #go to mcgill main page
    goto_main()
    time.sleep(4)

    for position in positions:
        update_course(position, courses)

#undo the below comment if setup is not done or if you want to add another directory/subdirectory
#setup(courses, sp)

update_courses([3],courses)




#ENTER CREDENTIALS + MICROSOFT APP
'''
email = driver.find_element_by_name("loginfmt")
email.send_keys("saif-eddine.abdelkefi@mail.mcgill.ca")
email.send_keys(Keys.RETURN)

time.sleep(5)
password = driver.find_element_by_id("passwordInput")
password.send_keys("Realmadrid123?")
password.send_keys(Keys.RETURN)

#waiting to approve on the app
time.sleep(20)

driver.find_element_by_id("idSIButton9").click()

'''

