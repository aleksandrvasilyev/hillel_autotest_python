import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_01():
    chrome_driver = Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get('https://demoqa.com/login')
    chrome_driver.find_element(By.XPATH, '//input[@id="userName"]').send_keys('aleksandr111')
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('7lB2Tw%Hxi_B')
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//button[@id="login"]').click()
    time.sleep(3)
    chrome_driver.close()
