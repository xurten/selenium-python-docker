from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Basepage(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.webdriver_wait = WebDriverWait(self.driver, 10)

    def click(self, selector, value):
        self.driver.find_element(selector, value).click()

    def send_keys(self, selector, selector_value, text):
        self.driver.find_element(selector, selector_value).send_keys(text)

    def close_driver(self):
        self.driver.close()
