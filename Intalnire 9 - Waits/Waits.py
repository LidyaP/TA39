from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()


#sleep()#opreste executia testului pt cate secunde ai dat
# chrome.implicitly_wait(5)#implicity waits
# last_name = WebDriverWait(chrome, 5).until(EC.presence_of_element_located(By.ID, 'last-name123')))
# last_name.send_keys('S')

# setam implicit_wait
# selenium va cauta toate elementele timp de x secunde inainte de a da eroare
chrome.implicitly_wait(8)

# navigam catare url
chrome.get('https://formy-project.herokuapp.com/form')

# pentru a calcula timpul de executie importam time, initalizam o variabila de start si una de final si facem diferenta
# start_time = time.time()
# start_time = time.time()
# try:
#     chrome.find_element(By.ID, 'first-name').send_keys('ELON')
#     chrome.find_element(By.ID, 'last-name2').send_keys('MUSK')
#     chrome.find_element(By.ID, 'job-title').send_keys('INJINER')
# except Exception as e:
#     end_time = time.time()
#     elapsed = end_time - start_time
#     print(elapsed)
#     print(e)

primul_element = chrome.find_element(By.ID, 'first-name')
primul_element.send_keys('ELON')
if primul_element:
    print('Elementul 1 a fost gasit')
else:
    print('Nu am gasit elementul')

al_doilea_element = chrome.find_element(By.ID, 'last-name')
al_doilea_element.send_keys('MUSK')
if al_doilea_element:
    print('Elementul 2 a fost gasit')
else:
    print('Nu am gasit elementul')

al_treilea_element = chrome.find_element(By.ID, 'job-title')
al_treilea_element.send_keys('TESTER')
if al_treilea_element:
    print('Elementul 3 a fost gasit')
else:
    print('Nu am gasit elementul')

sleep(5)
chrome.quit()