import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from POM.BasePage import BasePage
from utils import logger

log = logger.get_logger()

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    profile_img_xpath = "(//div[contains(@class,'gravatar-wrap')])[1]"
    Logout_xpath =  "//ul[@id='account-boxheader']//p[normalize-space()='Sign Out']"
    dobby_virtual_xpath = "//span[@aria-label='Chat Widget']"

    def profile_img_check(self):
        return self.is_element_visible("profile_img_xpath",self.profile_img_xpath)

    def click_profile_img(self):
        self.click_element("profile_img_xpath", self.profile_img_xpath)
        self.wait_for_JS()

    def click_logout_action(self):
        self.click_element("Logout_xpath",self.Logout_xpath)

    def dobby_is_present(self):
        return self.is_element_visible("dobby_virtual_xpath",self.dobby_virtual_xpath)