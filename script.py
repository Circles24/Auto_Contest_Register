import getpass
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


op = webdriver.firefox.options.Options()
op.headless = True
profile = webdriver.FirefoxProfile()
profile.set_preference("javascript.enabled", True)

driver = webdriver.Firefox(profile,options=op)
driver.get("http://www.codeforces.com/contests")
elem = WebDriverWait(driver,5).until(
	
	EC.presence_of_element_located((By.CSS_SELECTOR, "div.lang-chooser"))

	)

print ("elem.text")

def login():

	print("@ login")

	elem=driver.find_element_by_link_text('Enter').click()

	handle_elem = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.NAME, "handleOrEmail"))
	)

	handle = input("enter codeforces handle\n")
	password = getpass.getpass(prompt='Password: ') 
	
	handle_elem.send_keys(handle)
	driver.find_element_by_name('password').send_keys(password)
	driver.find_element_by_class_name('submit').submit()
	
	print("credentials submitted")

	handle_elem = WebDriverWait(driver,5).until(
		EC.presence_of_element_located((By.CSS_SELECTOR,"div.lang-chooser"))
		)

	input("press enter to continue")
	
	if "Logout" in driver.page_source:
            return True
	else:
	    print("invalid credentials")
	    
	    return False


if 'Enter' in elem.text:
    
    login()

    try:
        while True:

            elem=driver.find_element_by_class_name("datatable")
            elem.find_element_by_partial_link_text('Register').click()
            elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.submit"))
            )
            elem.submit()
          
    except NoSuchElementException :
        print ("no contest available for registration")
        pass
    finally:
    	driver.close()	             
	    


