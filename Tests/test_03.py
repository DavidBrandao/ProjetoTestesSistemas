import pytest

from Pages.LoanPage import LoanPage
from Pages.LoginPage import LoginPage


class Test03:

    # Test setup (Opens login page)
    @pytest.fixture()
    def setup(self, browser):
        # Login Page Instance
        self.login_page = LoginPage(browser=browser)
        # Open Login Page
        self.login_page.open_login_page()
        # Logando na aplicação
        self.login_page.login()

    def teste_retirar_emprestimo(self, setup, tear_down):
        # Instanciar a classe LoanPage
        self.loan_page = LoanPage(self.login_page.driver)

        # Acessar e verificar a tela de loan request
        assert self.loan_page.open_request_loan_page()

        # Realizar um emprestimo
        self.loan_page.apply_loan()

        # Verificar se o status da operação foi 'Approved'
        assert self.loan_page.verify_loan_status_approved()

        # Verificar se a mensagem de sucesso esta correta para o request
        assert self.loan_page.verify_loan_status_message()

    #Test TearDown (Closes driver)
    @pytest.fixture()
    def tear_down(self):
        yield
        self.login_page.QuitDriver()