from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(Browser):
    COOKIES_BUTTON = ()

    def wait_and_click_element(self, selector):
        WebDriverWait(self.chrom, 5).until(EC.presence_of_element_located(*selector))
        self.chrom.find_element(*selector).click()

    def accept_cookies(self):
        pass
        # TO BE IMPLEMENTED
