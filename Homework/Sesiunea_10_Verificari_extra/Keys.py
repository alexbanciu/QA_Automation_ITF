import  unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Key(unittest.TestCase):
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.implicitly_wait(2)

    USERNAME = (By.ID, 'username')

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
        username.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        username.send_keys(Keys.BACKSPACE)
        time.sleep(2)