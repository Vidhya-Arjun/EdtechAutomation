from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import get_logger
log = get_logger()

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _get_locator_type(self, locator_name):
        """Map locator name suffix to By type"""
        locator_map = {
            "_id": By.ID,
            "_name": By.NAME,
            "_xpath": By.XPATH,
            "_css": By.CSS_SELECTOR,
            "_class": By.CLASS_NAME,
            "_linktext": By.LINK_TEXT
        }

        for suffix, by_type in locator_map.items():
            log.info(f"by_type:{by_type}")
            if locator_name.endswith(suffix):
                return by_type
        raise ValueError(f"Unknown locator type for: {locator_name}")



    def is_element_clickable(self, locator_name, locator_value):
        try:
            log.info(f"Checking if element is clickable: {locator_name} with value: {locator_value}")

            self.wait.until(EC.element_to_be_clickable((self._get_locator_type(locator_name), locator_value)))
            return True
        except Exception as e:
            log.exception(f"is_element_clickable: element not clickable for {locator_name}={locator_value}: {e}")
            return False


    def click_element(self,locator_name,locator_value):
        log.info(f"Clicking element: {locator_name} with value: {locator_value}")
        element = self.get_element(locator_name,locator_value)
        element.click()

    def get_element(self, locator_name, locator_value):
        element = None
        try:
            log.info(f"element is available : {locator_name} with value: {locator_value}")
            element = self.wait.until(EC.visibility_of_element_located((self._get_locator_type(locator_name), locator_value)))
            return element
        except Exception as e:
            log.exception(f"get_element: element is not available {locator_name}={locator_value}: {e}")
            return element

    def type_text(self,locator_name,locator_value,text):
        log.info(f"Typing text: '{text}' into element: {locator_name} with value: {locator_value}")
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def retrieve_element_text(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.text

    def retrieve_list_of_element_text(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.text

    def is_element_visible(self,locator_name,locator_value):
        try:
            element = self.get_element(locator_name, locator_value)
            return element.is_displayed()
        except Exception as e:
            # Log the full exception traceback so failures are visible in logs while preserving original behaviour
            log.exception(f"is_element_visible: unexpected error while checking visibility for {locator_name}={locator_value}: {e}")
            return False

    def is_element_enabled(self,locator_name,locator_value):
        try:
            element = self.get_element(locator_name, locator_value)
            return element.is_enabled()
        except Exception as e:
            # Log the full exception traceback so failures are visible in logs while preserving original behaviour
            log.exception(f"is_element_enabled: unexpected error while checking enabled state for {locator_name}={locator_value}: {e}")
            return False

    def wait_for_JS(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            return True
        except TimeoutException:
            print("Timeout waiting for JavaScript/jQuery to load.")
            return False
