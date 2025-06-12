import os
import time

import pytest
from selenium.webdriver.common.by import By

from pages.sandbox.login_page import LoginPage

class TestPositiveScenarios():

    @pytest.mark.employee
    @pytest.mark.positive
    def test_get_list_employee(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])
        time.sleep(2)

        driver.get("https://semenenko.sandbox.first.institute/odoo/employees")
        time.sleep(2)

        employee_locator = driver.find_elements(By.CSS_SELECTOR, "span.fw-bold.fs-5")

        employees = [element.text for element in employee_locator]

        for employee in employees:
            print(employee)

        actual_employees = ['Abigail Peterson', 'Anita Oliver', 'Audrey Peterson', 'Beth Evans', 'Doris Cole',
                            'Eli Lambert', 'Ernest Reed', 'Jeffrey Kelly', 'Jennie Fletcher', 'Keith Byrd',
                            'Marc Demo', 'Mitchell Admin', 'Paul Williams', 'Rachel Perry', 'Randall Lewis', 'Ronnie Hart',
                            'Sharlene Rhodes', 'Tina Williamson', 'Toni Jimenez', 'Walter Horton']

        assert actual_employees == employees, f"The lists do not match!\nExpected: {actual_employees}\nActual: {employees}"