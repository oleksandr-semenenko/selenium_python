import pytest

from pages.sandbox.company_page import CompanyPage


class TestPositiveScenarios:
    @pytest.mark.positive
    @pytest.mark.company
    def test_open_documentation_page(self, driver, signed_as_admin):
        company_page = CompanyPage(driver)

        company_page.click()
        company_page.click_documentation()

        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])

        documentation_url = "https://www.odoo.com/documentation/18.0/"
        assert driver.current_url == documentation_url


    @pytest.mark.positive
    @pytest.mark.company
    def test_open_support_page(self, driver, signed_as_admin):
        company_page = CompanyPage(driver)

        company_page.click()
        company_page.click_support()

        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])

        support_url = "https://www.odoo.com/pricing#hosting=on_premise"
        assert driver.current_url == support_url
