from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage


class AdvancedSearchPage(BasePage):
    ENTER_KEYWORDS_OR_ITEM_NUMBER = ()
    KEYWORD_OPTIONS = ()
    EXCLUDE_WORDS_FROM_SEARCH = ()
    SEARCH_CATEGORIES = ()
    SEARCH_BUTTON = ()

    def enter_keywords_or_item_number(self):
        pass
        # TO BE IMPLEMENTED

    def select_keyword_options(self):
        pass
        # TO BE IMPLEMENTED

    def select_search_category(self):
        pass
        # TO BE IMPLEMENTED

    def exclude_words_from_search(self):
        pass
        # TO BE IMPLEMENTED

    def click_search_button(self):
        pass
        # TO BE IMPLEMENTED
