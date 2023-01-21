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

# # 1
chrome.get('https://www.phptravels.net/login')
input_list = chrome.find_elements(By.TAG_NAME, 'input')
input_list[0].send_keys('it.factory')
input_list[1].send_keys('123')

# 2
chrome.get('https://formy-project.herokuapp.com/form')
input_list = chrome.find_elements(By.TAG_NAME, 'Input')
# input_list[0].send_keys('Hello')
# input_list[1].send_keys('ITFactory	')
# input_list[2].send_keys('Tester')

# 3
# chrome.get('http://automationpractice.com/index.php?controller=contact')
# chrome.find_element(By.TAG_NAME, 'textarea').send_keys('Multumim!')
chrome.quit()