import time

from selenium.webdriver.common.by import By

from Pages.General import General


class LoanPage(General):

    url = 'https://parabank.parasoft.com/parabank/requestloan.htm'

    titleCssSelector = 'div h1.title'
    loanAmountID = 'amount'
    downPaymentID = 'downPayment'
    applyNowButtonCssSelector = "input[value='Apply Now']"
    loanStatusID = 'loanStatus'
    messageSuccessCssSelector = '.ng-scope p'
    messageErroClass = 'error'

    requestLoanMenuOption = 'Request Loan'
    titleText = 'Apply for a Loan'

    successLoanMessage = 'Congratulations, your loan has been approved.'
    failLoanMenssage = 'An internal error has occurred and has been logged.'



    def __init__(self, driver):
        super(LoanPage, self).__init__(driver=driver)

    def open_request_loan_page(self):
        # Abrir request loan page
        self.driver.find_element(By.LINK_TEXT, self.requestLoanMenuOption).click()

        # Verify page URL
        is_url = self.driver.current_url == self.url

        # Get page title
        element_title = self.driver.find_element(By.CSS_SELECTOR, self.titleCssSelector)

        # Verify page title
        is_title = element_title.text == self.titleText
        return is_url and is_title

    def apply_loan(self):
        # Preencher o campo Loan Amount
        self.driver.find_element(By.ID, self.loanAmountID).send_keys(100)

        # Preencher o campo Down Payment
        self.driver.find_element(By.ID, self.downPaymentID).send_keys(50)

        # Clicar no botão ApplyNow
        self.driver.find_element(By.CSS_SELECTOR, self.applyNowButtonCssSelector).click()

    def click_apply_now_button(self):
        # Procurar o botão apply now
        self.driver.find_element(By.CSS_SELECTOR, self.applyNowButtonCssSelector)

        # Clicar no botão ApplyNow
        self.driver.find_element(By.CSS_SELECTOR, self.applyNowButtonCssSelector).click()

    def verify_loan_status_approved(self):
        # Verificar o status (Approved)
        return self.driver.find_element(By.ID, self.loanStatusID).text == 'Approved'

    def verify_loan_status_message(self):
        # Verificar mensagem de sucesso
        return  self.driver.find_element(By.CSS_SELECTOR, self.messageSuccessCssSelector).text == self.successLoanMessage

    def verify_fields_empty(self):
        # Vericar o campo Loan Amount está vazio
        is_loan_amount = self.driver.find_element(By.ID, self.loanAmountID).text == ''

        # Vericar o campo Down Payment está vazio
        is_downPayment = self.driver.find_element(By.ID, self.downPaymentID).text == ''

        return is_loan_amount and is_downPayment

    def verify_erro_message(self):
        return self.driver.find_element(By.CLASS_NAME, self.messageErroClass).text == self.failLoanMenssage