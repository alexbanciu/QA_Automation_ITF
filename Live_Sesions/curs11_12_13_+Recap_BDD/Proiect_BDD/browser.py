from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    chrom = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    chrom.maximize_window()
    chrom.implicitly_wait(2)

    def close(self):
        self.chrom.delete_all_cookies()
        self.chrom.quit()
