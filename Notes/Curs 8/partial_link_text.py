import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome()
time.sleep(3)
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/")
time.sleep(2)
chrome.find_element(By.PARTIAL_LINK_TEXT,"Auth").click()
time.sleep(3)
chrome.quit()