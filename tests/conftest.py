import os

import pytest
from selenium.webdriver.common.by import By

from conftest import driver


@pytest.fixture()
def signed_in_user(driver):
    #driver.get("https://semenenko.sandbox.first.institute/web/login")
    driver.get(os.environ["FRONTEND_URL"] + "/web/login")

    driver.find_element(By.ID, "login").send_keys(os.environ["LOGIN"])
    driver.find_element(By.ID, "password").send_keys(os.environ["PASSWORD"])
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
    yield driver