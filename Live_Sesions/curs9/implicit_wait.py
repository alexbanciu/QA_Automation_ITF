from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.implicitly_wait(10)
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")

chrome.find_element(By.ID, "username").send_keys("tomsmith")
# chrome.find_element(By.ID, "usernames").send_keys("tomsmith") # = > "usernames" nu se gaseste...Vom avea eroare in consola, dupa ce sistemul asteapta 10 secunde...
# chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
chrome.find_element(By.ID, "passwords").send_keys("SuperSecretPassword!") # = > "passwords" nu se gaseste...Vom avea eroare in consola, dupa ce sistemul asteapta 10 secunde...

chrome.quit()

