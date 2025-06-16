import os

import pytest
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait

from pages.sandbox.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])
        WebDriverWait(driver, 10.0).until(
            url_to_be("https://semenenko.sandbox.first.institute/odoo/discuss")
        )

        assert (
            driver.current_url
            == "https://semenenko.sandbox.first.institute/odoo/discuss"
        ), "URL is not as expected"
