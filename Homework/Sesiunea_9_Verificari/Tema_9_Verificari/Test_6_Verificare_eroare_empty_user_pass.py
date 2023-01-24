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
    ERROR_MESSAGE=(By.XPATH,'//*[@id="flash"]')


    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(*self.FORM_AUTHENTICATION_LINK).click()
        self.chrome.implicitly_wait(7)


    def tearDown(self):
        self.chrome.quit()



    # Test 6 - Verificare eroare user/pass goale
    def test_mesaj_alerta(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.ERROR_MESSAGE))
        self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila')
        print(f'Eroarea este vizibila')