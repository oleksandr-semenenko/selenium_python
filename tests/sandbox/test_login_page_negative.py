import pytest

from pages.sandbox.login_page import LoginPage


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_login(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login("non_existing_user@example.com", "password_of_non_existing_user")

        assert login_page.is_login_error_displayed()