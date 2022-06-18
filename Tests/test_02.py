import time
import pytest

from Pages.UpdateProfilePage import UpdateProfilePage

class Test_2:

    def test_edit_field_zipcode(self, log_in):
          login_page, inventory_page = log_in

          self.update_profile_page = UpdateProfilePage(login_page.driver)
          assert self.update_profile_page.open_update_profile_page(), 'A tela de atualização do perfil não foi aberta encontrada!'
          assert self.update_profile_page.are_fields_profile_page(), 'A tela não apresentou todos os campo!'
          zipCodeText = self.update_profile_page.edit_zipCode_text_box()
          self.update_profile_page.presence_success_mens_until(), 'Mensagem de sucesso não exibida!'
          assert self.update_profile_page.has_update_message_success(), 'Mensagem de sucesso esta incorreta!'
          assert self.update_profile_page.open_update_profile_page(), 'A tela de atualização do perfil não foi aberta encontrada!'
          assert self.update_profile_page.check_ZipCode_change(zipCodeText), 'O campo changeZipcode não foi atualizado!'
