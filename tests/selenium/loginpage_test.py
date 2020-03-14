from unittest import TestCase

from pages.loginpage import Loginpage


class LoginPageTests(TestCase):
    successAlertMessage = "You logged into a secure area!"
    headingMessage = "Secure Area"
    page = None

    def setUp(self):
        self.page = Loginpage()

    def test_check_if_login_successful(self):
        self.page = self.page\
            .set_user_name(Loginpage.UserName) \
            .set_user_password(Loginpage.UserPassword) \
            .click_login()

        self.assertEqual(self.headingMessage, self.page.get_heading_text())
        self.assertEqual(self.successAlertMessage, self.page.get_alert_text()[:-1].strip())

    def tearDown(self):
        self.page.clear_page()