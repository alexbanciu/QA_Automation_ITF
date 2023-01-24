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
    USER_NAME=(By.ID,'username')
    PASSWORD=(By.ID,'password')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="flash"]')
    ERROR_CLOSED=(By.XPATH,'//*[@id="flash"]/a')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(*self.FORM_AUTHENTICATION_LINK).click()
        self.chrome.implicitly_wait(5)


    def tearDown(self):
        self.chrome.quit()


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