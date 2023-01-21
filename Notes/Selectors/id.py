
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
time.sleep(3)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form") # putem deschide un site
chrome.find_element(By.ID, "first-name").send_keys("Marian")
chrome.find_element(By.ID, "last-name").send_keys("Gheorghisor")
time.sleep(3)
chrome.quit() # inchide toata instanta browserului
# chrome.close() -> inchide un singur tab (cel activ) din instanta de browser