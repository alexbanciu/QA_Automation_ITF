from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# 3 dupa atribut valoare
chrome.get('https://www.phptravels.net/signup')
chrome.find_element(By.XPATH, '//input[@name="first_name"]').send_keys('IT')
chrome.find_element(By.XPATH, '//input[@placeholder="Last Name"]').send_keys('Factory')
chrome.find_element(By.XPATH, '//input[@type="password"]').send_keys('07')

# 3 dupa textul de pe element
chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.XPATH, '//a[text()="Best Sellers"]').click()
# chrome.find_element(By.XPATH, '//a[text()="Contact us"]').click()

# 1 dupa partial text
chrome.get('https://www.phptravels.net/blog')
full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Independent Cultures")]').text # => aici nu pot da click?
print(full_text)

# 1 cu SAU, folosind pipe |
chrome.get('https://www.phptravels.net/login')
chrome.find_element(By.XPATH, '//input[@name="email"] | //a[@name="email"]').send_keys("itfactory@gmail.com")

# 1 cu *
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.XPATH, '//*[@id="autocomplete"]').send_keys('ok')

# 1 in care sa folosesti parent::
# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.XPATH, '//label[text()="Job title"]/parent::strong')

# 1 in care sa folosesti fratele anterior sau de dupa (la alegere)
# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.XPATH, '//label[text()="Job title"]/parent::strong/following-sibling::input').send_keys("QA Automation Tester")
# sleep(2)

# 1 funcție ca și cea de la clasă prin care să poti alege prin parametru cu ce element vreai să interacționez.
def select_years_of_experience(select_by_visible_text):
    years_of_experience_dropdpwn = Select(chrome.find_element(By.ID, 'select-menu'))
    years_of_experience_dropdpwn.select_by_visible_text(select_by_visible_text)

# select_years_of_experience("0-1")

sleep(4)
chrome.quit()