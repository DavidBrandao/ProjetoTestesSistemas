import time

import pytest
from Pages.General import General
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from Pages.ProductsPage import ProductsPage


class TestLogin:

    # Test setup (Opens login page)
    @pytest.fixture()
    def setup(self, browser):
        #Login Page Instance
        self.login_page = LoginPage(browser=browser)
        # Open Login Page
        self.login_page.open_login_page()

    # Verify error message for trying to log in without user and password
    def test_fluxo_compra(self, setup, tear_down):
        # Logando na aplicação
        self.login_page.login()

        # Verificar se o usuário esta logado
        self.main_page = MainPage(self.login_page.driver)
        assert self.main_page.verifyUserIsLogged(), 'O usuário não logou no sistema'

        # Acessar o Menu de Vestidos

        self.main_page.clickDressesButton()
        time.sleep(3)
        # Adicionar o primeiro vestido da lista ao carrinho
        # Ir para a tela de checkout
        # Concordar com os temos de serviço
        # Realizar pagamento com cartão de credito
        # Verificar que o pagamento foi realizado com sucesso


    # Test TearDown (Closes driver)
    @pytest.fixture()
    def tear_down(self):
        yield
        self.login_page.QuitDriver()
