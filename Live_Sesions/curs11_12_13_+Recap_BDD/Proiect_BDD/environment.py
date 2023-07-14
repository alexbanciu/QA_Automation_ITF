from browser import Browser
from pages.ebay_homepage import Home_page
from pages.ebay_advanced_search_page import AdvancedSearchPage


def before_all(context):
    #  * beefore_all este o metoda recunoscuta de libraria behave si care se
    #  va executa inainte de toate testele
    #  * context este ca o cutiuta in care vom stoca toate atributele ce pot fi folosite in alte fisiere
    context.browser = Browser()
    context.home_page_object = Home_page()
    context.advanced_search_object = AdvancedSearchPage()


def after_all(context):
    # * after_all este o metoda recunoscuta de libraria behave si care se
    #     #  va executa dupa de toate testele
    context.browser.close()
