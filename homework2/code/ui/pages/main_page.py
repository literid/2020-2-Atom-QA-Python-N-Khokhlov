from ui.pages.base_page import BasePage
from ui.locators.basic_locators import MainPageLocators
from ui.pages.company_page import CompanyPage
from ui.pages.segment_page import SegmentPage

class MainPage(BasePage):
    locators = MainPageLocators()

    def go_to_company_page(self):
        self.click(MainPageLocators.COMPANY)
        return CompanyPage(driver=self.driver)

    def go_to_segment_page(self):
        self.click(MainPageLocators.SEGMENT)
        return SegmentPage(driver=self.driver)