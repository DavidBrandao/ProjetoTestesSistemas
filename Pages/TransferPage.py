import time
from selenium.webdriver.common.by import By
from Pages.General import General


class TransferPage(General):

    # Url da página
    url = 'https://parabank.parasoft.com/parabank/transfer.htm'
    # Lateral Menu
    transferFundsOption = 'Transfer Funds'
    # Page title
    titleCssSelector = 'div h1.title'
    amountID = 'amount'
    transferButtonCssSelector = 'input[value="Transfer"]'
    titleCompleteCssSelector = '.ng-scope h1'
    titleSuccessText = 'Transfer Complete!'
    fromAccountID = 'fromAccountId'
    toAccountID = 'toAccountId'

    def __init__(self, driver):
        super(TransferPage, self).__init__(driver=driver)

    def open_transfer_page(self):
        # Clicar no item transfer funds do menu lateral
        self.driver.find_element(By.LINK_TEXT, self.transferFundsOption).click()

        # Verificar URL da página
        is_url = self.driver.current_url == self.url

        # Verificar o titulo da página
        element_text = self.driver.find_element(By.CSS_SELECTOR, self.titleCssSelector).text
        is_title = element_text == self.transferFundsOption

        return is_url and is_title

    def transfer_funds_same_account(self):
        time.sleep(1)
        self.driver.find_element(By.ID, self.amountID).send_keys('10')
        self.driver.find_element(By.CSS_SELECTOR, self.transferButtonCssSelector).click()

    def verify_title_sucess(self):
        time.sleep(1)
        return self.driver.find_element(By.CSS_SELECTOR, self.titleCompleteCssSelector).text == self.titleSuccessText

    def verify_transfer_data_visible(self):
        return (self.driver.find_element(By.ID, self.amountID).is_displayed() and
                self.driver.find_element(By.ID, self.fromAccountID).is_displayed() and
                self.driver.find_element(By.ID, self.toAccountID).is_displayed())
