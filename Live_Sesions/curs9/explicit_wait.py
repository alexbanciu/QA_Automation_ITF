from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Chrome()

chrome.get("https://the-internet.herokuapp.com/login")
chrome.maximize_window()

username = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.ID, 'username')))
# username = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.ID, 'usernames')))
# = > "usernames" nu se gaseste...Vom avea eroare in consola, dupa ce sistemul asteapta 5 secunde...
username.send_keys('tomsmith')

# password = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.ID, 'password')))
password = WebDriverWait(chrome, 7).until(EC.presence_of_element_located((By.ID, 'passwords')))
# = > "passwords" nu se gaseste...Vom avea eroare in consola, dupa ce sistemul asteapta 7 secunde...
password.send_keys('SuperSecretPassword!')

chrome.quit()
