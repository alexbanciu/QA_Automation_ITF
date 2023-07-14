from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser


class Base_page(Browser):

    def wait_for_elem(self, by, selector):
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((by, selector)))
