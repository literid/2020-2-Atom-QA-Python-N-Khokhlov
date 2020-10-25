from tests.base import BaseCase
from ui.pages.main_page import MainPage
from selenium.common.exceptions import TimeoutException
import pytest
import time


class Test(BaseCase):
    def test_authorization_pos(self, login: MainPage):
        login.find(login.locators.BALANCE)

    def test_authorization_neg(self):
        email, password = "wrong_mail@mail.ru", "wrong_password"
        self.base_page.click(self.base_page.locators.LOGIN_BUTTON)
        email_elem = self.base_page.find(locator=self.base_page.locators.EMAIl_INPUT)
        email_elem.clear()
        email_elem.send_keys(email)
        passw_elem = self.base_page.find(locator=self.base_page.locators.PASSWORD_INPUT)
        passw_elem.clear()
        passw_elem.send_keys(password)
        self.base_page.click(self.base_page.locators.AUTH_BUTTON)
        self.base_page.find(self.base_page.locators.INVALID_LOGIN_TEXT)

    def test_company_creating(self, login: MainPage, my_company_name):
        company_page = login.go_to_company_page()
        company_page.create_company(my_company_name)
        company_page.find(company_page.locators.MYCOMPANY_NAME_IN_LIST)

    def test_segment_creating(self, login: MainPage, my_segment_name):
        segment_page = login.go_to_segment_page()
        segment_page.create_segment(my_segment_name)
        segment_page.find(segment_page.locators.MY_SEGMENT_NAME_LOC)

    def test_segment_deleting(self, login: MainPage, my_segment_name):
        segment_page = login.go_to_segment_page()
        segment_page.create_segment(my_segment_name)
        segment_page.delete_segment(my_segment_name)
        time.sleep(1)
        with pytest.raises(TimeoutException):
            segment_page.find(segment_page.locators.MY_SEGMENT_NAME_LOC, timeout=1)
