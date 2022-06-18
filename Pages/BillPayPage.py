import time
from selenium.webdriver.common.by import By
from Pages.General import General


class BillPage(General):

    # Url da página
    url = 'https://parabank.parasoft.com/parabank/billpay.htm'

    # Lateral menu
    billPayMenuOption = 'Bill Pay'

    # Page title
    titleCssSelector = 'div h1.title'

    # Form items ID
    payeeTextBoxName = 'payee.name'
    addressTextBoxName = 'payee.address.street'
    cityTextBoxName = 'payee.address.city'
    stateTextBoxName = 'payee.address.state'
    zipCodeTextBoxName = 'payee.address.zipCode'
    phoneTextBoxName = 'payee.phoneNumber'
    accountTextBoxName = 'payee.accountNumber'
    verifyAccountTextBoxName = 'verifyAccount'
    amountTextBoxName = 'amount'
    sendPaymentButttonCssSelector = 'input[value="Send Payment"]'

    # Complete Screen Data
    payeeNameID = 'payeeName'
    amountID = 'amount'
    fromAccountID = 'fromAccountId'

    titleText = 'Bill Payment Service'


    def __init__(self, driver):
        super(BillPage, self).__init__(driver=driver)

    def open_bill_payment_page(self):
        # Clicar no item bill pay do menu lateral
        self.driver.find_element(By.LINK_TEXT, self.billPayMenuOption).click()

        # Verificar URL da página
        is_url = self.driver.current_url == self.url

        # Verificar o titulo da página
        element_title = self.driver.find_element(By.CSS_SELECTOR, self.titleCssSelector)
        is_title = element_title.text == self.titleText

        return is_url and is_title

    def fill_payment_form(self):
        self.driver.find_element(By.NAME, self.payeeTextBoxName).send_keys('Cesar School')
        self.driver.find_element(By.NAME, self.addressTextBoxName).send_keys('Marco Zero')
        self.driver.find_element(By.NAME, self.cityTextBoxName).send_keys('Recife')
        self.driver.find_element(By.NAME, self.stateTextBoxName).send_keys('PE')
        self.driver.find_element(By.NAME, self.zipCodeTextBoxName).send_keys('000000')
        self.driver.find_element(By.NAME, self.phoneTextBoxName).send_keys('000000')
        self.driver.find_element(By.NAME, self.accountTextBoxName).send_keys('22557')
        self.driver.find_element(By.NAME, self.verifyAccountTextBoxName).send_keys('22557')
        self.driver.find_element(By.NAME, self.amountTextBoxName).send_keys('10')
        self.driver.find_element(By.CSS_SELECTOR, self.sendPaymentButttonCssSelector).click()

    def verify_bill_was_paid(self):
        time.sleep(1)
        return (self.driver.find_element(By.ID, self.payeeNameID).is_displayed() and
                self.driver.find_element(By.ID, self.amountID).is_displayed() and
                self.driver.find_element(By.ID, self.fromAccountID).is_displayed())
