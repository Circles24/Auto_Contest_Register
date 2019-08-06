import os
import getpass
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def getFirefox():

	op = webdriver.firefox.options.Options()
	op.headless = True

	profile = webdriver.FirefoxProfile()
	profile.set_preference("javascript.enabled", True)

	webEngine = webdriver.Firefox(profile,options=op)

	return webEngine


webEngine = getFirefox()
elem = 'just_a_place_holder'
data_file_location = "/home/kenzo/Prj/Auto_reg"


def fetchCodeforces():

    global elem

    webEngine.get("http://www.codeforces.com/contests")
    elem = WebDriverWait(webEngine,5).until(
	    
	    EC.presence_of_element_located((By.CSS_SELECTOR, "div.lang-chooser"))

	    )

def login():

	print("@ login")
	
	global elem

	elem = webEngine.find_element_by_link_text('Enter').click()

	handle_elem = WebDriverWait(webEngine, 5).until(
	EC.presence_of_element_located((By.NAME, "handleOrEmail"))
	)
	
	curr_path = os.getcwd()
	
	#if curr_path == '/usr/bin'
	if curr_path is '/home/kenzo/Prj/Auto_reg':
	       f = open("/home/kenzo/test/test.sh",'r') 
	       data = f.read()
	       print(data)
	       return False
    
	else :
	
	    handle = input("enter codeforces handle\n")
	    password = getpass.getpass(prompt='Password: ') 
	
	handle_elem.send_keys(handle)
	webEngine.find_element_by_name('password').send_keys(password)
	webEngine.find_element_by_class_name('submit').submit()
	
	print("credentials submitted")

	handle_elem = WebDriverWait(webEngine,5).until(
		EC.presence_of_element_located((By.CSS_SELECTOR,"div.lang-chooser"))
		)
	
	if "Logout" in webEngine.page_source:
            return True
	else:
	    
	    return False



def main():

    attempts = 0

    while True:
    
        global elem
    
        print("attempting auto registration")
        
        attempts += 1
        fetchCodeforces()
        print("attempt :: ",attempts)
                
        if 'Enter' in elem.text:
            
            print("fetched Codeforces")  
                      
            while True:
                if login() is True:
                    break
                else :
                    print("failed")
                    
                    choice = input("y/n")
                    if choice is not 'y':
                        return
            
            try:

                elem = webEngine.find_element_by_class_name("datatable")
                elem.find_element_by_partial_link_text('Register').click()
                elem = WebDriverWait(webEngine, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.submit"))
                )
                elem.submit()
                  
                print("Sucessfull registered")
            
            except NoSuchElementException :
                print ("no contest available for registration")
                break
            
            except Exception :
                print("Some Exception occured")
                
            finally:
            	webEngine.close()
            
            break            
        
        elif attempts == 10:
           
           print("failed attempts :: 10")
           return
        
        
           



main()


