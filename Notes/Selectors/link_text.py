import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Link text = textul care este pus peste un link
Linkurile pe un site sunt definite prin intermediul unei ancore (tag-ul a)
Un element de tip ancora are urmatoarele componente:
1. tag-ul de inceput (a)
2. linkul catre care se face navigarea (href = "valoare")
3. textul care este afisat peste link (linktext)
4. tag-ul de sfarist (/a)
<a href="/checkboxes">Checkboxes</a>
"""
chrome = webdriver.Chrome()
time.sleep(3)
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/")
chrome.find_element(By.LINK_TEXT, "Checkboxes").click()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Form Authentication").click()
chrome.quit()