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

# navigam catre un url
chrome.get('https://the-internet.herokuapp.com/login')

# 1
username = chrome.find_element(By.ID, 'username')
username.send_keys('itfactory')

# 2
password = chrome.find_element(By.ID, 'password')
password.send_keys('123')

# navigam catre un url
chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

# 3
# email_create = chrome.find_element(By.ID, 'email_create')
# email_create.send_keys('itfactory@gmail.com')
chrome.quit()