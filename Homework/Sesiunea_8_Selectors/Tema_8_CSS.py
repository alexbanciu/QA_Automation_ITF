import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

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