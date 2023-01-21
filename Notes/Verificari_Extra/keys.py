import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Key(unittest.TestCase):
    USERNAME = (By.ID, 'username')
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_select_all(self):
        username = self.chrome.find_element(*self.USERNAME)
        username.send_keys('Alabalaportocala')
        time.sleep(2)
        username.clear()
        time.sleep(2)
        username.send_keys('Alabalaportocala_Alabalaportocala')
        time.sleep(2)
        username.send_keys(Keys.COMMAND, 'a')
        time.sleep(2)
        username.send_keys(Keys.BACKSPACE)
        time.sleep(2)

        listt = ['Ala', 'bala', 'porto', 'cala']
        for elem in listt:
            username.send_keys(elem)
            time.sleep(1)

        username.send_keys(Keys.ARROW_LEFT, 'T')
        time.sleep(2)
        username.send_keys(Keys.ARROW_LEFT)
        time.sleep(3)
        username.send_keys(Keys.BACKSPACE)
        time.sleep(5)


