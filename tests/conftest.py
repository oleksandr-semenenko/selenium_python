import os

import pytest

from pages.sandbox.login_page import LoginPage


@pytest.fixture()
def signed_as_admin(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])
    return driver
