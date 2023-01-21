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


#chrome.get('https://formy-project.herokuapp.com/')
#chrome.find_element(By.PARTIAL_LINK_TEXT, 'Press').click()

chrome.get('https://www.techlistic.com/')
chrome.find_element(By.ID,"ez-accept-all").click()
sleep(5)
chrome.find_element(By.ID,"cookieChoiceDismiss").click()
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Choosing Kotlin').click()
chrome.quit()