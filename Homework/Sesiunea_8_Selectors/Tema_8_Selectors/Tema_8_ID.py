import time

from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()

#By.ID
chrome.get("https://phptravels.net/")
chrome.maximize_window()
chrome.find_element(By.ID, "autocomplete").send_keys("Sibiu")
time.sleep(2)
chrome.find_element(By.ID, "autocomplete2").send_keys("Barcelona")
time.sleep(2)
chrome.find_element(By.ID, "departure").click()
time.sleep(2)