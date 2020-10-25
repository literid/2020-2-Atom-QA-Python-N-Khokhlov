import os.path
from ui.pages.base_page import BasePage
from ui.locators.basic_locators import CompanyPageLocators
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_banner_path():
    dir_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(dir_path, "images", "mybanner.jpg")


LINK = "https://target.my.com/dashboard"
BUDGET_PER_DAY = 100
BUDGET_TOTAL = 100000


class CompanyPage(BasePage):
    locators = CompanyPageLocators()

    def create_company(self, my_company_name):
        self.click(self.locators.CREATE_COMPANY_BUTTON)
        self.click(self.locators.TRAFFIC_BUTTON)
        link_input = self.find(self.locators.LINK_INPUT)
        link_input.clear()
        link_input.send_keys(LINK)
        comp_name: WebElement = self.wait(6).until(EC.element_to_be_clickable(self.locators.COMPANY_NAME_FIELD))
        comp_name.clear()
        comp_name.send_keys(my_company_name)
        budget_per_day: WebElement = self.find(self.locators.BUDGET_PER_DAY)
        budget_per_day.clear()
        budget_per_day.send_keys(BUDGET_PER_DAY)
        budget_total: WebElement = self.find(self.locators.BUDGET_TOTAL)
        budget_total.clear()
        budget_total.send_keys(BUDGET_TOTAL)
        self.click(self.locators.BANNER)
        image_upload: WebElement = self.find(self.locators.UPLOAD_IMAGE)
        image_upload.send_keys(get_banner_path())
        self.click(self.locators.FINALLY_CREATE_COMPANY)
        self.locators.MYCOMPANY_NAME_IN_LIST = (By.XPATH, f"//*[@title='{my_company_name}']")
        return

