import time

import pytest

from pages.sandbox.login_page import LoginPage

class TestPositiveScenarios():

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login("oleksandr.semenenko@icloud.com", "AyEzXNKZBEma84e")
        time.sleep(2)  # I know that is not good solution, but it's not work with implicit wait

        assert driver.current_url == "https://semenenko.sandbox.first.institute/odoo/discuss", \
            "URL is not as expected"