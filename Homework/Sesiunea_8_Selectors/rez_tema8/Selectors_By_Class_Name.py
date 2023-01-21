from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/autocomplete')
lista_elemente = chrome.find_elements(By.CLASS_NAME,"form-control")
# lista_elemente[0].send_keys("Romania")
# lista_elemente[1].send_keys("Strada Lalelelor")
# lista_elemente[2].send_keys("Cluj")
chrome.quit()