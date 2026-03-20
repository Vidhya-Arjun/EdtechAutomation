from selenium.webdriver.support import expected_conditions as EC
from POM.BasePage import BasePage
from Test.conftest import driver
from utils import logger

log = logger.get_logger()

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    Login_Button_xpath = "(//button[@id='login-btn'])[1]"
    Sign_Up_xpath = "(//button[normalize-space()='Sign up'])[1]"
    LiveClasses_xpath = "//div[@id='solutions']/p[normalize-space()='LIVE Classes']"
    Courses_xpath = "//div[@id='solutions']/p[normalize-space()='Courses']"
    Practice_xpath = "//div[@id='solutions']/p[normalize-space()='Practice']"
    SignUp_page_button_xpath = "//a[@id='signup-btn']"

    def login_button_isAccessible(self):
        return self.is_element_clickable("Login_Button_xpath",self.Login_Button_xpath)

    def signup_button_isAccessible(self):
        return self.is_element_clickable("Sign_Up_xpath",self.Sign_Up_xpath)

    def click_login_button(self):
        self.click_element("Login_Button_xpath", self.Login_Button_xpath)

    def signup_button_check(self):
        self.click_element("Sign_Up_xpath",self.Sign_Up_xpath)
        return self.is_element_clickable("SignUp_page_button_xpath", self.SignUp_page_button_xpath)


    def LiveClasses_section_is_accessible(self):

        return (self.is_element_visible("LiveClasses_xpath",self.LiveClasses_xpath) and
                self.is_element_enabled("LiveClasses_xpath",self.LiveClasses_xpath))

    def Courses_section_is_accessible(self):

        return (self.is_element_visible("Courses_xpath", self.Courses_xpath) and
                self.is_element_enabled("Courses_xpath", self.Courses_xpath))

    def Practice_section_is_accessible(self):

        return (self.is_element_visible("Practice_xpath", self.Practice_xpath) and
                self.is_element_enabled("Practice_xpath", self.Practice_xpath))
