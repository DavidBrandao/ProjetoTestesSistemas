import pytest

from Pages.LoginPage import LoginPage


class Test03:

    # Test setup (Opens login page)
    @pytest.fixture()
    def setup(self, browser):
        # Login Page Instance
        self.login_page = LoginPage(browser=browser)
        # Open Login Page
        self.login_page.open_login_page()

    def teste_retirar_emprestimo(self, setup, tear_down):


    # Test TearDown (Closes driver)
    @pytest.fixture()
    def tear_down(self):
        yield
        self.login_page.QuitDriver()