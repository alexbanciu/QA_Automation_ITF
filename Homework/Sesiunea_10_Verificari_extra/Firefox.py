import unittest
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


class Firefox(unittest.TestCase):
    USERNAME = 'admin'
    PASSWORD = 'admin'

    def setUp(self) -> None:
        self.firefox = webdriver.Firefox
        self.firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.firefox.maximize_window()

    def tearDown(self) -> None:
        self.firefox.quit()

    def test_auth(self):
        self.firefox.get("https://" + self.USERNAME + ":" + self.PASSWORD + "@the-internet.herokuapp.com/basic_auth")
        time.sleep(4)