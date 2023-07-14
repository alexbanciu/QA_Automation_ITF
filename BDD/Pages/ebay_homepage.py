from pyparsing import results
from selenium.webdriver.support.select import Select

from BDD.Pages.base_page import Base_page


class Home_page(Base_page):
    SEARCH_TEXTBOX = ()
    SEARCH_BUTTON = ()
    SEARCH_CATEGORIES = ()
    ADVANCED_SEARCH_LINK = ()
    SEARCH_RESULTS = ()

    def navigate_to_homepage(self):
        self.chrome.get("https://www.ebay.com/")

    def insert_search_value(self, product_name):
        self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys(product_name)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def choose_category(self,category_name):
        category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
        category_dropdown.select_by_visible_text(category_name)


    def click_advanced_link(self):
        self.wait_and_click_element(*self.ADVANCED_SEARCH_LINK)

    def check_search_results(self, nr_of_results):
        partial_result = self.chrome.find_element(*self.SEARCH_RESULTS).text
        result = partial_result.replace(",", "")
        assert int(results) >=int(nr_of_results), f'Error: Results are incorrect. Expected: {nr_of_results}'