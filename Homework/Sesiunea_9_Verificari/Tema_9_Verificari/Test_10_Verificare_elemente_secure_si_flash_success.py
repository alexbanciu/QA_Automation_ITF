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
    SUCCESS_MESSAGE=(By.XPATH,'//*[@class="flash success"]')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(*self.FORM_AUTHENTICATION_LINK).click()
        self.chrome.implicitly_wait(7)


    def tearDown(self):
        self.chrome.quit()


    # Test 10 - Verificare elemente secure si flash succes
    def test_verif_secure(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        url_dupa_logare=self.chrome.current_url
        self.assertTrue("secure" in url_dupa_logare,'Noul url nu contine secure')
        WebDriverWait(self.chrome,10).until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
        assert self.chrome.find_element(*self.SUCCESS_MESSAGE).is_displayed() == True, 'Not displayed'