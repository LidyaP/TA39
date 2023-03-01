# pip install selenium
# pip install webdriver-manager

from time import sleep # ca sa stea pagina deschisa cat ne dorim noi, pt asta se face importul
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager #deschide chrome
from selenium.webdriver.common.by import By #asta cauta

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')


#selector by ID
try:
    first_name = chrome.find_element(By.ID, 'first-name')
    first_name.send_keys('Lidia')
except Exception as e:
    print('ID-ul introdus nu este corect')
print('Am ajuns aici')
chrome.find_element(By.ID, 'first-name').send_keys('TEST AUTOMATION')

sleep(10)
chrome.quit()#inchide fereastra de Chrome