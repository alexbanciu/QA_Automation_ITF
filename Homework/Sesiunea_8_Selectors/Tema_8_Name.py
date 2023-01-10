import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
chrome.find_element(By.NAME,"firstname").send_keys("Banciu")
time.sleep(1)
time.sleep(1)
chrome.find_element(By.NAME,"lastname").send_keys("Alexandru")
time.sleep(1)
chrome.find_element(By.NAME,"continents")
time.sleep(1)

chrome.quit()