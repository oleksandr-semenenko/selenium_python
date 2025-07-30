import os

import pytest

from pages.sandbox.login_page import LoginPage


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_login(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN_NEGATIVE"], os.environ["PASSWORD_NEGATIVE"])

        assert login_page.is_login_error_displayed()