"""
Libraria unittest este o librarie care suporta crearea de teste rulabile direct in interiorul clasei
Se implementeaza prin mostenirea clasei TestCAse din libraria unittest
Orice clasa de teste trebuie sa mosteneasca clasa TestCase si sa aiba urmatoarele particularitati
1. Metoda setup -> toate activitatile care trebuie sa fie executate inainte de ORICE TEST din clasa respectiva
2. Metoda teardown -> toate activitatile care trebuie sa fie executate dupa ORICE TEST din clasa respectiva
3. toate metodele de test trebuie sa aiba prefixul test_
Metode de rulare:
1. Click dreapta pe fisier + Run
2. Din terminal
2.1. click dreapta pe numele pachetului (TREBUIE SA FIE PACHET) -> Copy Path / Reference -> Absolute Path
2.2. cd <calea pe care ati copiat-o>
2.3. pytest nume_fisier_de_rulat
instalare pytest: pip install pytest
"""

import unittest
# from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By


class Alerts(unittest.TestCase):
    JS_ALERT_BUTTON = (By.XPATH, '//*[text()="Click for JS Alert"]')
    JS_CONFIRM_BUTTON = (By.XPATH, "//*[text()='Click for JS Confirm']")
    JS_PROMPT_BUTTON = (By.XPATH, "//*[text()='Click for JS Prompt']")
    ALERT_ACTION_MESSAGE = (By.ID, "result")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()

    @unittest.skip
    def test_js_alert_accept(self):
        self.chrome.find_element(*self.JS_ALERT_BUTTON).click()
        # steluta are functie de DESPACHETARE A TUPLULUI
        # metoda find_element asteapta doi parametri: metoda de cautare, valoare de cautare
        # daca nu scriem *, atunci metoda va primi un singur parametru de tip tuplu si se va returna eroare

        js_alert = self.chrome.switch_to.alert
        js_alert.accept()
        js_alert_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = 'You successfully clicked an alert'
        assert js_alert_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_alert_text}"

    @unittest.skip
    def test_js_confirm_accept(self):
        self.chrome.find_element(*self.JS_CONFIRM_BUTTON).click()
        js_confirm = self.chrome.switch_to.alert
        js_confirm.accept()
        js_confirm_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = 'You clicked: Ok'
        assert js_confirm_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_confirm_text}"

    @unittest.skip
    def test_js_confirm_cancel(self):
        self.chrome.find_element(*self.JS_CONFIRM_BUTTON).click()
        js_confirm = self.chrome.switch_to.alert
        js_confirm.dismiss()
        js_confirm_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = 'You clicked: Cancel'
        assert js_confirm_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_confirm_text}"

    def test_js_prompt_accept_no_text_insert(self):
        self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
        js_prompt = self.chrome.switch_to.alert
        js_prompt.accept()
        js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = 'You entered:'
        assert js_prompt_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_prompt_text}"

    def test_js_prompt_cancel_no_text_inserted(self):
        self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
        js_prompt = self.chrome.switch_to.alert
        js_prompt.dismiss()
        js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = 'You entered: null'
        assert js_prompt_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_prompt_text}"

    def test_js_prompt_accept_text_insert(self):
        self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
        js_prompt = self.chrome.switch_to.alert
        js_prompt.send_keys("test")
        js_prompt.accept()
        js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = 'You entered: test'
        assert js_prompt_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_prompt_text}"

    def test_js_prompt_cancel_text_inserted(self):
        self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
        js_prompt = self.chrome.switch_to.alert
        js_prompt.send_keys("test")
        js_prompt.dismiss()
        js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = 'You entered: null'
        assert js_prompt_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_prompt_text}"


"""
!!! Notes:
self.chrome.find_element(*self.JS_ALERT_BUTTON) => self.chrome.find_element(By.XPATH,'//*[text()="Click for JS Alert"]')
self.chrome.find_element(self.JS_ALERT_BUTTON) => self.chrome.find_element((By.XPATH,'//*[text()="Click for JS Alert"]'))
"""
