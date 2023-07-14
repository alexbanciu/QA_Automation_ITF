from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    chrome.maximize_window()
    chrome.implicitly_wait(2)

    def close(self):
        self.chrome.delete_all_cookies()
        self.chrome.quit()