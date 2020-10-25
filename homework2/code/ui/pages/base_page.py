from ui.locators import basic_locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

RETRY_COUNT = 5


class BasePage(object):
    locators = basic_locators.BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=10):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=10):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < RETRY_COUNT:
                    pass
        raise

    def wait(self, timeout=10):
        return WebDriverWait(driver=self.driver, timeout=timeout)



