from pages.basepage import Basepage
from selenium.webdriver.common.by import By


class Loginpage(Basepage):
    LoginPageUrl = "https://the-internet.herokuapp.com/login"
    UserName = "tomsmith"
    UserPassword = "SuperSecretPassword!"

    def __init__(self):
        super().__init__()
        self.driver.get(self.LoginPageUrl)

    def set_user_name(self, name):
        self.send_keys(By.ID, "username", name)
        return self

    def set_user_password(self, password):
        self.send_keys(By.ID, "password", password)
        return self

    def click_login(self):
        self.click(By.XPATH, "//button[@class='radius']")
        return self

    def get_heading_text(self):
        return self.driver.find_element(By.TAG_NAME, "h2").text.strip()

    def get_alert_text(self):
        return self.driver.find_element(By.ID, "flash").text

    def clear_page(self):
        self.close_driver()
