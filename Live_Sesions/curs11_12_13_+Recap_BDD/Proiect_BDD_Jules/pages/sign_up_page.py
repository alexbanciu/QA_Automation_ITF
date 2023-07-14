from pages.base_page import Base_page
from selenium.webdriver.common.by import By
from time import sleep

class Sign_up_page(Base_page):
    SIGN_UP = (By.XPATH, "//*[@id='root']/div/div[2]/form/div/div[4]/a")
    PERSONAL_BUTTON = (By.XPATH, "//input[@value='personal']")
    CONTINUE_BUTTON = (By.XPATH, "//button[@data-test-id='select-account-continue-btn']")
    INPUT = (By.XPATH, "//input[@type='text']")
    # INPUT2 = (By.XPATH, "//*[@id='root']/div/div[4]/div[2]/div/div[2]/div/div/input")
    FIRST_NAME_CONTINUE_BUTTON = (By.XPATH, "//button[@data-test-id='first-name-continue-btn']")
    LAST_NAME_CONTINUE_BUTTON = (By.XPATH, "//button[@data-test-id='last-name-continue-btn']")
    EMAIL_CONTINUE_BUTTON = (By.XPATH, "//button[@data-test-id='email-continue-btn']")

    def navigate_to_sign_in_page(self):
        self.chrome.get('https://jules.app/')

    def navigate_to_sign_up_page(self):
        self.chrome.find_element(*self.SIGN_UP).click()
        sleep(2)

    def click_personal_button(self):
        self.chrome.find_element(*self.PERSONAL_BUTTON).click()
        sleep(2)

    def click_continue_button(self):
        self.chrome.find_element(*self.CONTINUE_BUTTON).click()
        sleep(2)

    def send_first_name(self, name):
        self.chrome.find_element(*self.INPUT).send_keys(name)
        sleep(2)

    def click_continue_first_name_button(self):
        self.chrome.find_element(*self.FIRST_NAME_CONTINUE_BUTTON).click()
        sleep(3)

    def send_last_name(self, name):
        self.chrome.find_element(*self.INPUT).send_keys(name)
        sleep(4)

    def click_continue_last_name_button(self):
        self.chrome.find_element(*self.LAST_NAME_CONTINUE_BUTTON).click()
        sleep(4)

    def send_email(self, email):
        self.chrome.find_element(*self.INPUT).send_keys(email)
        sleep(2)

    def click_continue_email_button(self):
        self.chrome.find_element(*self.LAST_NAME_CONTINUE_BUTTON).click()

    def check_error_message_email(self):
        expected = "Please enter a valid email address."
        actual = self.chrome.find_element(By.XPATH, "//*[@id='root']/div/div[4]/div[2]/div/div[2]/div/p").text
        assert expected ==actual

