import time
import pytest
from Pages.LoanPage import LoanPage
from Pages.LoginPage import LoginPage


class Test04:

    # Test setup (Opens login page)
    @pytest.fixture()
    def setup(self, browser):
        # Login Page Instance
        self.login_page = LoginPage(browser=browser)
        # Open Login Page
        self.login_page.open_login_page()
        # Logando na aplicação
        self.login_page.login()

    def teste_tentativa_relizar_emprestimo_sem_valores(self, setup, tear_down):
        # Instanciar a classe LoanPage
        self.loan_page = LoanPage(self.login_page.driver)

        # Acessar e verificar a tela de loan request
        assert self.loan_page.open_request_loan_page(), 'A página Loan não foi aberta'

        # Verificar se os campos estão vazios
        assert self.loan_page.verify_fields_empty(), 'Os campos estão preenchidos'

        # Clicando no botão Apply Now
        self.loan_page.click_apply_now_button()

        # Verificar a mensagem de erro está correta
        assert self.loan_page.verify_erro_message(), 'A mensagem de erro está incorreta'

    # Test TearDown (Closes driver)
    @pytest.fixture()
    def tear_down(self):
        yield
        self.login_page.QuitDriver()
