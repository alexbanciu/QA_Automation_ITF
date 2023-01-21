import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chromepage = webdriver.Chrome()
chromepage.get("https://www.phptravels.net/")
#css id
chromepage.find_element(By.CSS_SELECTOR, "#Tab").click()
time.sleep(2)
# css atribut = valoare
chromepage.find_element(By.CSS_SELECTOR, "input[name='checkout']")
time.sleep(2)

#css clasa
chromepage.find_element(By.CSS_SELECTOR, ".hero-wrappe")
time.sleep(2)
chromepage.find_element(By.CSS_SELECTOR, "#fadein > section.hero-wrappe")
time.sleep(2)
chromepage.quit()