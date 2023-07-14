from BDD.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class Base_page(Browser):
    def wait_and_click_element(self, selector):
        WebDriverWait(self.chrome,5).until(EC.presence_of_element_located(* selector))
        self.chrome.find_element(* selector).click()
# metoda accept cookies

# metoda wait and click element