import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_01():
    chrome_driver = Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.maximize_window()
    chrome_driver.get('https://demoqa.com/login')
    login = 'aleksandr111'
    password = '7lB2Tw%Hxi_B'
    chrome_driver.find_element(By.XPATH, '//input[@id="userName"]').send_keys(login)
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
    time.sleep(2)
    chrome_driver.find_element(By.XPATH, '//button[@id="login"]').click()
    time.sleep(3)
    chrome_driver.close()
