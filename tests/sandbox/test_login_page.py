import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver



class TestPositiveScenarios():

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):

        driver = webdriver.Chrome()
        time.sleep(3)


        driver.get("https://semenenko.sandbox.first.institute/web/login")
        time.sleep(5)

        username_locator = driver.find_element(By.ID, "login")
        username_locator.send_keys("oleksandr.semenenko@icloud.com")

        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("AyEzXNKZBEma84e")

        login_button_locator = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        login_button_locator.click()
        time.sleep(5)

        actual_url = driver.current_url
        assert actual_url == "https://semenenko.sandbox.first.institute/odoo/discuss", "URL is not as expected"

        driver.quit()
