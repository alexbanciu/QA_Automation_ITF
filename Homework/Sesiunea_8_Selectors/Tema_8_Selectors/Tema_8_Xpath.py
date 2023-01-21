import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chromepage = webdriver.Chrome()
chromepage.get("https://www.phptravels.net/")
chromepage.maximize_window()
#Xpath atribut valoare
chromepage.find_element(By.XPATH, "//*[@id='back-to-top']")
time.sleep(2)

chromepage.find_element(By.XPATH, "//*[@id='loading']")
time.sleep(2)

# dupa textul de pe element
chromepage.find_element(By.XPATH, "//a[text()='Privacy Policy']")
time.sleep(2)
chromepage.find_element(By.XPATH, "//a[text()='How to Book']")
time.sleep(2)
chromepage.find_element(By.XPATH, "//a[text()='FAQ']")
time.sleep(2)

# dupa text partial
chromepage.find_element(By.XPATH, "//a[contains(text(), 'flig')]")

#  (xpath)[1]
chromepage.find_element(By.XPATH, '//*[@id="fadein"]/section[1]')
time.sleep(2)


chromepage.quit()