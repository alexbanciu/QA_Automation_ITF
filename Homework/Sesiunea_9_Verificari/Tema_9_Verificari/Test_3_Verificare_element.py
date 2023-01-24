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
    H2_ELEMENT=(By.XPATH,'//h2')


    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(*self.FORM_AUTHENTICATION_LINK).click()
        self.chrome.implicitly_wait(5)


    def tearDown(self):
        self.chrome.quit()



    # Test 3 - Verificare element
    def test_element(self):
        actual = self.chrome.find_element(*self.H2_ELEMENT).text
        print(f'Denumirea elementului este {actual}')
        expected = 'Login Page'
        self.assertEqual(actual, expected, f' Denumirea elementului este {actual}, dar ar fi trebuit sa fie {expected}')