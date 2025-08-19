import os

import pytest

from pages.sandbox.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        assert driver.current_url == os.environ["FRONTEND_URL"] + "/odoo/discuss"