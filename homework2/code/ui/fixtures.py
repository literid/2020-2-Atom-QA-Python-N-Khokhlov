import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
import random
import string


class UnsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope="function")
def driver(config):
    browser = config["browser"]
    version = config["version"]
    url = config["url"]
    remote_server = config["remote_server"]
    if browser == "chrome":
        if remote_server == "http:///wd/hub/":
            driver = webdriver.Chrome(executable_path=ChromeDriverManager(version=version).install())
        else:
            driver = webdriver.Remote(command_executor=remote_server,
                                      desired_capabilities={"browserName": "chrome", "version": "85"})
    else:
        raise UnsupportedBrowserException(f"browser {browser} is not supported")

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope="function")
def login(base_page, config):
    email, password = config["email"], config["password"]
    base_page.click(base_page.locators.LOGIN_BUTTON)
    email_elem = base_page.find(locator=base_page.locators.EMAIl_INPUT)
    email_elem.clear()
    email_elem.send_keys(email)
    passw_elem = base_page.find(locator=base_page.locators.PASSWORD_INPUT)
    passw_elem.clear()
    passw_elem.send_keys(password)
    base_page.click(base_page.locators.AUTH_BUTTON)
    yield MainPage(base_page.driver)
    base_page.click(base_page.locators.LOGOUT_FIELD)
    base_page.click(base_page.locators.EXIT_BUTTON)


@pytest.fixture()
def my_segment_name(length=7):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@pytest.fixture()
def my_company_name(length=7):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
