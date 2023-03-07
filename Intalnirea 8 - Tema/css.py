from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get('https://formy-project.herokuapp.com/scroll')

driver.find_element(By.CSS_SELECTOR, 'input#name').send_keys('Cristina')
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys(' Dumitru')
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="MM/DD/YYYY"]').send_keys('03/07/2023')
sleep(2)
driver.find_element(By.ID, 'logo').click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Web Form').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'div input[placeholder*="first name"]').send_keys('Cristina')
driver.find_element(By.CSS_SELECTOR, 'div input[placeholder*="last name"]').send_keys('Dumitru')
driver.find_element(By.CSS_SELECTOR, 'div input[placeholder*="job title"]').send_keys('Casier')
sleep(5)
