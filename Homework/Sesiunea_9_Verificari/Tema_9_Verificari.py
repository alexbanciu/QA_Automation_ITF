from unittest import TestCase
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import unittest
import HTMLTestRunner

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
# Definirea metodei de tearDown
    def tearDown(self) -> None:
        self.chrome.quit()