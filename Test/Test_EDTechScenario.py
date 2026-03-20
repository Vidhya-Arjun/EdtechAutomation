import time

import pytest

from POM.AccountPage import AccountPage
from POM.LoginPage import LoginPage
from POM.ProfilePage import ProfilePage
from utils import logger

log = logger.get_logger()


@pytest.mark.smoke
def test_is_valid_url(driver,config):

    """To check the url's existence and to check whether it is active"""
    log.info("Testing is_valid_url")
    assert driver.current_url.__eq__(config['base_url']),"URL mismatch"


def test_validate_title_of_the_page(driver,config):

    """To check the title is as per matches the expected results"""
    log.info("Testing title_of_the_page")
    assert driver.title.__eq__(config['title']),"Title mismatch"

def test_login_button_check(driver,config):

    """Verify visibility and clickability of the Login button."""
    account = AccountPage(driver)
    log.info("Testing login button clickability")
    assert account.login_button_isAccessible(), "Login button should be clickable"

def test_SignUp_button_check(driver,config):

    """Verify visibility and clickability of the SignUp button."""
    account = AccountPage(driver)
    log.info("Testing SignUp clickability")
    assert account.signup_button_isAccessible(), "SignUp button should be clickable"
    log.info("Testing Sign up button clickability")
    assert account.signup_button_check(),"SignUp navigation not happened for registering new User"
    log.info("Testing Sign up button navigation link workflow")


def test_validate_navigation_of_signUp_buttton(driver,config):

    """Verify navigation to the Sign-In page via the Sign-Up button."""
    account = AccountPage(driver)
    assert account.signup_button_check(),"SignUp navigation not happened for registering new User"

def test_valid_login_scenario(driver,config):
    account = AccountPage(driver)
    login = LoginPage(driver)
    profile = ProfilePage(driver)

    account.click_login_button()
    login.enter_username(config['username'])
    login.enter_password(config['password'])
    login.click_login_btn()

    assert profile.profile_img_check(), f"Expected 'sourceUri' in URL, but got: {driver.current_url}"
    log.info(f"Successfully navigated to dashboard page: {driver.current_url}")

def test_valid_login_scenario(driver,config):
    account = AccountPage(driver)
    login = LoginPage(driver)
    profile = ProfilePage(driver)

    account.click_login_button()
    login.enter_username(config['username'])
    login.enter_password(config['password'])
    login.click_login_btn()

    assert profile.profile_img_check(), f"Expected 'sourceUri' in URL, but got: {driver.current_url}"
    log.info(f"Successfully navigated to dashboard page: {driver.current_url}")

def test_valid_login_scenario(driver,config):
    account = AccountPage(driver)
    login = LoginPage(driver)
    profile = ProfilePage(driver)

    account.click_login_button()
    login.enter_username(config['invalid_username'])
    login.enter_password(config['invalid_password'])
    login.click_login_btn()
    error_msg = login.display_error_msg()
    assert error_msg.__contains__(config['error_message_invalid']), f"Expected 'Invalid Username or Password' in URL, but got: {error_msg}"
    log.info(f"Successfully navigated to dashboard page: {error_msg}")


def test_learning_path_section(driver,config):
    account = AccountPage(driver)
    assert account.Courses_section_is_accessible(), f"Expected 'Courses  is not acessible, check for the page"
    log.info(f"Courses section is accessible")
    assert account.Practice_section_is_accessible(), f"Expected 'Practice  is not acessible, check for the page"
    log.info(f"Practice section is accessible")
    assert account.LiveClasses_section_is_accessible(), f"Expected 'Live Section  is not acessible, check for the page"
    log.info(f"Live Classes section is accessible")

def test_dobby_guvi_assistant_check(driver,config):
    account = AccountPage(driver)
    login = LoginPage(driver)
    profile = ProfilePage(driver)

    account.click_login_button()
    login.enter_username(config['username'])
    login.enter_password(config['password'])
    login.click_login_btn()

    assert profile.profile_img_check(), f"Expected 'sourceUri' in URL, but got: {driver.current_url}"
    log.info(f"Successfully navigated to dashboard page: {driver.current_url}")

    assert profile.dobby_is_present() ,f"Expected virtual assistant dobby is present,but it is no available"


def test_logout_functionality(driver,config):
    account = AccountPage(driver)
    login = LoginPage(driver)
    profile = ProfilePage(driver)

    account.click_login_button()
    login.enter_username(config['username'])
    login.enter_password(config['password'])
    login.click_login_btn()
    print("title",driver.title)
    profile.click_profile_img()

    profile.click_logout_action()

    assert driver.title.__eq__(config['title']),\
        f"Expected base URL, but got: {driver.current_url}"