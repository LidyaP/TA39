from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/form')


first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys('Lidia')
input_list = chrome.find_elements(By.CLASS_NAME, 'form-control')
input_list[1].send_keys('TEST ALADIN')



sleep(10)
chrome.quit()
