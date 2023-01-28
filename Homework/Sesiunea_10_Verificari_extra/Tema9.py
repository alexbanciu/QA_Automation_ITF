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
    FORM_AUTHENTICATION_LINK = (By.XPATH, '//a[text()="Form Authentication"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    H2_ELEMENT = (By.XPATH, '//h2')
    HREF_LINK = (By.XPATH, '//a[@href="http://elementalselenium.com/"]')
    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    # ERROR_MESSAGE=(By.XPATH,'//div[@id="flash"]')
    # sau
    ERROR_MESSAGE = (By.XPATH, "//div[normalize-space(contains(text(),'Your username is invalid'))]")
    ERROR_CLOSED = (By.XPATH, '//a[@class="close"]')
    LABEL_LIST = (By.XPATH, '//label')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="flash success"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')
    ELEM_H4 = (By.XPATH, '//h4[@class="subheader"]')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(*self.FORM_AUTHENTICATION_LINK).click()
        self.chrome.implicitly_wait(7)

    def tearDown(self):
        self.chrome.quit()

    # @unittest.skip
    # Test 1 - Verificare URL
    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual, 'URL-ul nu este corect')

    # @unittest.skip
    # Test 2 - Verificare page title
    def test_page_title(self):
        actual = self.chrome.title
        expected = 'The Internet'
        self.assertEqual(expected, actual, f' Titlul paginii este {actual}, dar ar fi trebuit sa fie {expected}')

    # @unittest.skip
    # Test 3 - Verificare element
    def test_element(self):
        actual = self.chrome.find_element(*self.H2_ELEMENT).text
        print(f'Denumirea elementului este {actual}')
        expected = 'Login Page'
        self.assertEqual(actual, expected, f' Denumirea elementului este {actual}, dar ar fi trebuit sa fie {expected}')

    # @unittest.skip
    # Test 4 - Verificare Login button
    def test_login_displayed(self):
        button = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(button.is_displayed(), 'Butonul de LOGIN nu este vizibil')

    # @unittest.skip
    # Test 5 - Verificare href link
    def test_href_link(self):
        actual_link = self.chrome.find_element(*self.HREF_LINK).get_attribute('href')
        assert actual_link == 'http://elementalselenium.com/', 'Link-ul este gresit'
        print('Link-ul verificat este corect')

    # @ unittest.skip
    # Test 6 - Verificare eroare user/pass goale
    def test_mesaj_alerta(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.ERROR_MESSAGE))
        self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila')

    # @ unittest.skip
    # Test 7 - Verificare mesaj eroare
    def test_mesaj_eroare(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tom')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR_MESSAGE).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

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

    # @ unittest.skip
    # Test 9 - Verificare lista label
    def test_lista_label(self):
        elem_lista = self.chrome.find_elements(*self.LABEL_LIST)
        i = 0
        is_username_text_correct = False
        is_password_text_correct = False
        while i < len(elem_lista):
            if elem_lista[i].text == 'Username':
                is_username_text_correct = True
            elif elem_lista[i].text == 'Password':
                is_password_text_correct = True
            i += 1
        assert is_username_text_correct == True
        assert is_password_text_correct == True

    # @ unittest.skip
    # Test 10 - Verificare elemente secure si flash succes
    def test_verif_secure(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        url_dupa_logare = self.chrome.current_url
        self.assertTrue("secure" in url_dupa_logare, 'Noul url nu contine secure')
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
        assert self.chrome.find_element(*self.SUCCESS_MESSAGE).is_displayed() == True

    # @ unittest.skip
    # Test 11 - Verificare login - logout
    def test_verif_login_logout(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        WebDriverWait(self.chrome, 10).until(EC.url_contains('/login'))
        url_dupa_delogare = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        assert url_dupa_delogare == expected_url, f'Invalid url: {url_dupa_delogare} este diferit de {expected_url}'