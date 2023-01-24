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
    USER_NAME=(By.ID,'username')
    PASSWORD=(By.ID,'password')
    LABEL_LIST=(By.XPATH,'//label')

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
    # Test 9 - Verificare lista label
    def test_lista_label(self):
        global is_username_text_correct, is_password_text_correct
        elem_lista=self.chrome.find_elements(*self.LABEL_LIST)
        i = 0

        while i<len(elem_lista):
            if elem_lista[i].text=='Username':
                is_username_text_correct = True
            elif elem_lista[i].text=='Password':
                is_password_text_correct = True
            i += 1
        assert is_username_text_correct == True
        assert is_password_text_correct == True