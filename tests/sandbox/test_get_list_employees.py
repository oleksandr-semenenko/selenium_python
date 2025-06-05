import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPositiveScenarios():
    def test_get_list_employee(self):

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

        driver.get("https://semenenko.sandbox.first.institute/odoo/employees")
        time.sleep(10)

        employee_locator = driver.find_elements(By.CSS_SELECTOR, "span.fw-bold.fs-5")

        employees = [el.text for el in employee_locator]

        for employee in employees:
            print(employees)

        actual_employees = ['Abigail Peterson', 'Anita Oliver', 'Audrey Peterson', 'Beth Evans', 'Doris Cole',
                            'Eli Lambert', 'Ernest Reed', 'Jeffrey Kelly', 'Jennie Fletcher', 'Keith Byrd',
                            'Marc Demo', 'Mitchell Admin', 'Paul Williams', 'Rachel Perry', 'Randall Lewis', 'Ronnie Hart',
                            'Sharlene Rhodes', 'Tina Williamson', 'Toni Jimenez', 'Walter Horton']

        assert actual_employees == employees