import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")
"""
CSS = stands for Cascading Style Sheets => used to format the layout of a webpage
Referinta studiu suplimentar: https://www.w3schools.com/cssref/css_selectors.php
Cum sa gandim un selector?
1. # -> cautare dupa id
2. . -> cautare dupa clasa
3. daca prcedem # sau . de numele unui tag, atunci sistemul va cauta elementele cu tag-ul respectiv si id-ul /clasa respectiva
4. Putem sa cautam elemente cu un anumit tag cu filtrare de tipul [atribut = "valoare"]
5. Putem sa cautam primul copil al unui element cu caracterul >
6. Putem sa cautam orice copil al unui element daca separam tag-ul elementul de copilul sau prin spatiu
7. Daca vrem sa cautam primul copil al unui element putem sa specificam first-of-type
8. Daca vrem sa cautam ultimul copil al unui element putem sa specificam last-of-type
9. Daca vrem as cautam un copil care nu este nici primul nici ultimul putem sa folosim nth-of-type(al_catalea_element_este)
10. Daca vrem sa gasim un frate ulterior ne putem folosi de caracterul + 
"""

chrome.find_element(By.CSS_SELECTOR,"#first-name").send_keys("Anton")
# am facut cautare dupa id
chrome.find_element(By.CSS_SELECTOR,"#last-name").send_keys("Anton")
time.sleep(2)
chrome.find_element(By.CSS_SELECTOR,"#last-name").clear()
time.sleep(2)
# am facut cautare dupa atribut = valoare
chrome.find_element(By.CSS_SELECTOR,"input[placeholder='Enter last name']").send_keys("Pann")
time.sleep(2)
# am facut cautare dupa clasa
chrome.find_elements(By.CSS_SELECTOR,".form-control")[2].send_keys("Tester")
text_label_last_name = chrome.find_element(By.CSS_SELECTOR,"strong > label[for='last-name']").text
# assert condition [, Error Message]
assert text_label_last_name == "Last name",f"Error, Expected - Last name - , Actual: {text_label_last_name}"
chrome.find_element(By.CSS_SELECTOR,"div.input-group>div:nth-of-type(2) input").click()
chrome.find_element(By.CSS_SELECTOR,"div.input-group>div:last-of-type input").click()
education_label = chrome.find_element(By.CSS_SELECTOR,"div.input-group>div:first-of-type label").text
assert education_label == "Highest level of education",f"Error, expected:Highest level of education, Actual {education_label}"
college_education = chrome.find_element(By.CSS_SELECTOR,"div.input-group>div:nth-of-type(3)").text
assert college_education == "College",f"Error: Expected: College, actual {college_education}"
chrome.find_element(By.CSS_SELECTOR,"div.form-group > div:nth-of-type(2) > strong + input").send_keys("following sibling")
time.sleep(1)
chrome.quit()