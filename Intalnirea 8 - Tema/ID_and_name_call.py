from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.maximize_window()

driver.get('https://www.techlistic.com/p/selenium-practice-form.html?utm_content=cmp-true')
sleep(1)
driver.find_element(By.ID, 'ez-accept-all').click()
sleep(2)
link_test = driver.find_element(By.NAME, 'firstname')
link_test.send_keys('Lidia')
driver.find_element(By.NAME, 'lastname').send_keys('Popa')
driver.find_element(By.ID, 'sex-1').click()
driver.find_element(By.ID, 'exp-6').click()
# driver.find_element(By.ID, 'submit').click()
sleep(8)