import utilities.custom_logger.logger_file as cl
import logging
from base.basepage import basepage


class loginpage(basepage):
    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _user_name = 'txtName'
    _password = 'txtPassword'
    _login_link = 'btnLogin'

    def enter_username(self, username):
        self.enter_text(username, self._user_name)

    def enter_password(self, password):
        self.enter_text(password, self._password)

    def click_on_login_button(self):
        self.click_on_login_button()

    def login(self, username="", password=""):
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_login_button()
