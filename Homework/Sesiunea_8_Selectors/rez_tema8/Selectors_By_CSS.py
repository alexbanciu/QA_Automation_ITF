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

# 1 dupa ID
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input#autocomplete').send_keys('Andrei')

# 2 dupa clasa
chrome.get('https://www.phptravels.net/signup')
chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('Muresanu')

# 3 atribut=valoare_partiala
chrome.get('https://www.phptravels.net/signup')
chrome.find_element(By.CSS_SELECTOR, 'input[placeholder*="Last"]').send_keys('ITFactory')
chrome.quit()