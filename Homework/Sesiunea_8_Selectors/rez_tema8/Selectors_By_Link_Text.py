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
chrome.get('https://www.phptravels.net/')
chrome.find_element(By.LINK_TEXT, 'Blog').click()

# 2
# chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
# chrome.find_element(By.LINK_TEXT, 'Contact us').click()

# 3
# chrome.get('https://formy-project.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT, 'Checkbox').click()
chrome.quit()