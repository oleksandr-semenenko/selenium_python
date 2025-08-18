import os

import pytest
from selenium.webdriver.common.by import By

from conftest import driver
from pages.sandbox.login_page import LoginPage


@pytest.fixture()
def signed_as_admin(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])
    #driver.get("https://semenenko.sandbox.first.institute/web/login")
    # driver.get(os.environ["FRONTEND_URL"] + "/web/login")
    #
    # driver.find_element(By.ID, "login").send_keys(os.environ["LOGIN"])
    # driver.find_element(By.ID, "password").send_keys(os.environ["PASSWORD"])
    # driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
    #yield driver
    return driver