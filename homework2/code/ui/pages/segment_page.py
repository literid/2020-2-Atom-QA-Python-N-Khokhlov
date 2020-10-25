from ui.pages.base_page import BasePage
from ui.locators import basic_locators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class SegmentPage(BasePage):
    locators = basic_locators.SegmentPageLocators()

    def create_segment(self, my_segment_name):
        try:
            self.click(self.locators.CREATE_SEGMENT_BUTTON2, timeout=1)
        except TimeoutException:
            self.click(self.locators.CREATE_SEGMENT_BUTTON1, timeout=1)

        self.click(self.locators.APPS_AND_GAMES_BUTTON)
        self.click(self.locators.PLAYED_AND_PAYED_BUTTON)
        self.click(self.locators.ADD_SEGMENT)
        segment_name = self.find(self.locators.SEGMENT_NAME_FIELD)
        segment_name.clear()
        segment_name.send_keys(my_segment_name)
        self.click(self.locators.SUBMIT_SEGMENT)
        self.locators.MY_SEGMENT_NAME_LOC = (By.XPATH,
                               f"//div[@class='ReactVirtualized__Grid__innerScrollContainer'] // a[@title='{my_segment_name}']")
        return

    def delete_segment(self, my_segment_name):
        search = self.find(self.locators.SEARCH_BUTTON)
        search.send_keys(my_segment_name)
        self.click(self.locators.UNDER_SEARCH_FIELD)
        self.click(self.locators.DELETE_BUTTON)
        self.click(self.locators.CONFIRM_REMOVE_BUTTON)
        return
