import time

from selenium import webdriver
from selenium.webdriver.common.by import By

''' Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri '''



chrome = webdriver.Chrome()
time.sleep(3)
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/")
chrome.find_element(By.LINK_TEXT, "Frames").click()
time.sleep(3)
chrome.back()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Forgot Password").click()
time.sleep(3)
chrome.back()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Geolocation").click()
time.sleep(3)
chrome.quit()