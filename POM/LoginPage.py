from POM.BasePage import BasePage
from utils import logger

log = logger.get_logger()

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    Username_id = "email"
    Password_id = "password"
    LoginButton_id= "login-btn"
    error_msg_xpath ="//div[@class='invalid-feedback is-invalid'][1]"


    def enter_username(self, username):
        self.type_text("Username_id", self.Username_id, username)

    def enter_password(self, password):
        self.type_text("Password_id", self.Password_id, password)

    def click_login_btn(self):
        self.click_element("LoginButton_id", self.LoginButton_id)

    def display_error_msg(self):
        error_msg = self.retrieve_element_text("error_msg_xpath",self.error_msg_xpath)
        return error_msg
