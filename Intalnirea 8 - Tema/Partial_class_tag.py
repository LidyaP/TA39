from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get('https://formy-project.herokuapp.com/')
sleep(1)
link_test = driver.find_element(By.LINK_TEXT, 'Modal')
link_test.click()
driver.find_element(By.LINK_TEXT, 'Modal').click()
sleep(2)
driver.find_element(By.ID, 'modal-button').click()
sleep(2)
driver.find_element(By.CLASS_NAME, 'close').click()
sleep(2)
driver.find_element(By.ID, 'logo').click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Upload').click()
sleep(2)
driver.find_element(By.ID, 'logo').click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Web Form').click()
sleep(2)
input_list = driver.find_elements(By.TAG_NAME, 'input')
input_list[0].send_keys('Ioana')
input_list[1].send_keys('Marinescu')
sleep(5)