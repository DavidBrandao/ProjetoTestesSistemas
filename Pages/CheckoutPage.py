from selenium.webdriver.common.by import By

from Pages.General import General


class CheckoutPage(General):

    titleClassName = 'title'
    continueButtonID = 'continue'
    errorContainer = 'error-message-container'

    checkoutTitle = 'CHECKOUT: YOUR INFORMATION'
    errorMessage = 'Error: First Name is required'

    def __init__(self, driver):
        super(CheckoutPage, self).__init__(driver=driver)

    def get_page_title(self):
        return self.driver.find_element(By.CLASS_NAME, self.titleClassName).text

    def click_continue_button(self):
        self.driver.find_element(By.ID, self.continueButtonID).click()

    def get_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, self.errorContainer).text
