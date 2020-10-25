import pytest
from ui.pages.base_page import BasePage
from ui import fixtures


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
