import time

from selenium.webdriver.common.by import By

from Pages.General import General

class OpenAccountPage(General):
    url = 'https://parabank.parasoft.com/parabank/openaccount.htm'

    # ID and ClassName List
    openAccountTitleCssSelector = 'div h1.title'
    openAccountButtonCssSelector = "input[value='Open New Account']"
    messageSuccessCssSelector = '.ng-scope p'
    newAccountIdTextID = 'newAccountId'

    openAccountText = 'Open New Account'

    def __init__(self, driver):
        super(OpenAccountPage, self).__init__(driver=driver)

    def open_new_account_page(self):
        self.driver.find_element(By.LINK_TEXT, self.openAccountText).click()
        return self.is_page(self.URL, self.openAccountText)

    def create_new_account(self):
        # Clicar no botão de criar nova conta
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.openAccountButtonCssSelector).click()

        # (Aguardar entrar na tela de conta criada) trocar sleep por wait no elemento openAccountTitleCssSelector
        time.sleep(2)

        # Validar a mensagem de sucesso para a criação de conta
        textSuccess = self.driver.find_element(By.CSS_SELECTOR, self.messageSuccessCssSelector).text
        assert textSuccess == 'Congratulations, your account is now open.'

        # Validar o ID da nova conta criada
        return int(self.driver.find_element(By.ID, self.newAccountIdTextID).text)

