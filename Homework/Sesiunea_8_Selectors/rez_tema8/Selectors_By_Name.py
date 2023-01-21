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

# 1
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.NAME, 'search_query').send_keys('Bluza')

# 2
chrome.get('https://www.phptravels.net/signup')
chrome.find_element(By.NAME, 'phone').send_keys('0760131653')

# 3
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.NAME, 'email').send_keys('itfactory@gmail.com')
chrome.quit()