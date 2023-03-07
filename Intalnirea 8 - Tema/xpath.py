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
driver.find_element(By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input').send_keys('I')
sleep(2)
driver.find_element(By.XPATH, '//*[@id="tool-0"]').click()
sleep(5)