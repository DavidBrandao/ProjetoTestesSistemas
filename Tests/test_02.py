import pytest
from Pages.LoginPage import LoginPage
from Pages.UpdateProfilePage import UpdateProfilePage

class Test02:

    # Test setup (Opens login page)
    @pytest.fixture()
    def setup(self, browser):
        #Login Page Instance
        self.login_page = LoginPage(browser=browser)
        # Open Login Page
        self.login_page.open_login_page()
        # Logando na aplicação
        self.login_page.login()


    def test_atualizar_informacoes_contato(self, setup, tear_down):
        # Instanciar classe UpdateProfilePage
        self.update_page = UpdateProfilePage(self.login_page.driver)

        # Acessar e verificar a tela de atualizar informações
        assert self.update_page.open_update_profile_page()

        # Verificar os campos estão disponiveis para atualização
        assert self.update_page.are_fields_visible()

        # Alterar informação do zip code
        newZipCode = self.update_page.edit_zipCode_text_box()

        # Verificar existencia da mensagem de sucesso
        assert self.update_page.verify_success_message_is_displayed()

        # Verificar mensagem de sucesso
        assert self.update_page.verify_update_message()

        # Acessar novamente a tela de atualizar informações
        assert self.update_page.open_update_profile_page()

        # Validar que a informação foi atualizada
        assert self.update_page.check_ZipCode_change(newZipCode)

    # Test TearDown (Closes driver)
    @pytest.fixture()
    def tear_down(self):
        yield
        self.login_page.QuitDriver()
