import time

import pytest

from Pages.BillPayPage import BillPage
from Pages.LoginPage import LoginPage


class Test05:
    # Test setup (Opens login page)
    @pytest.fixture()
    def setup(self, browser):
        # Login Page Instance
        self.login_page = LoginPage(browser=browser)
        # Open Login Page
        self.login_page.open_login_page()
        # Logando na aplicação
        self.login_page.login()

    def teste_pagar_conta(self, setup, tear_down):
        # Instanciar a classe Bill Pay
        self.bill_page = BillPage(self.login_page.driver)

        # Acessar e verificar a tela de bill payment
        assert self.bill_page.open_bill_payment_page()

        # Preencher o pagamento da conta
        self.bill_page.fill_payment_form()

        # Verificar que o pagamento foi realizado com sucesso
        assert self.bill_page.verify_bill_was_paid()


    # Test TearDown (Closes driver)
    @pytest.fixture()
    def tear_down(self):
        yield
        self.login_page.QuitDriver()