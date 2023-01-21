import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random



class Login(unittest.TestCase):
    FORM_AUTHENTICATION_LINK=(By.XPATH,'//a[text()="Form Authentication"]')
    LOGIN_BUTTON=(By.XPATH,'//*[@id="login"]/button/i')
    H2_ELEMENT=(By.XPATH,'//h2')
    HREF_LINK=(By.XPATH,'//a[@href="http://elementalselenium.com/"]')
    USER_NAME=(By.ID,'username')
    PASSWORD=(By.ID,'password')
    # ERROR_MESSAGE=(By.XPATH,'//div[@id="flash"]')
    # sau
    ERROR_MESSAGE = (By.XPATH, "//div[normalize-space(contains(text(),'Your username is invalid'))]")
    ERROR_CLOSED=(By.XPATH,'//a[@class="close"]')
    LABEL_LIST=(By.XPATH,'//label')
    SUCCESS_MESSAGE=(By.XPATH,'//div[@class="flash success"]')
    LOGOUT_BUTTON=(By.XPATH,'//a[@href="/logout"]')
    ELEM_H4=(By.XPATH,'//h4[@class="subheader"]')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(*self.FORM_AUTHENTICATION_LINK).click()
        self.chrome.implicitly_wait(7)


    def tearDown(self):
        self.chrome.quit()

    # @ unittest.skip
    # Test 8 - Verificare inchidere mesaj eroare
    def test_inchidere_mesaj_eroare(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(5)
        self.chrome.find_element(*self.ERROR_CLOSED).click()
        sleep(5)
        try:
            self.chrome.find_element(*self.ERROR_CLOSED)
        except NoSuchElementException:
            print("The text is not visible on the page! It's ok")