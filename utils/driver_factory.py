from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(browser):
    if browser == "chrome":
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)
        driver.implicitly_wait(5)
        return driver

    elif browser == "firefox":
        options = Options()
        options.add_argument("-private")
        return webdriver.Firefox()
    elif browser == "safari":
        return webdriver.Safari()
    elif browser == "opera":
        return webdriver.Opera()
    elif browser == "edge":
        return webdriver.Edge()
    elif browser == "ie":
        return webdriver.Ie()
    else:
        raise ValueError("Unsupported browser")