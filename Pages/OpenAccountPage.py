from selenium.webdriver.common.by import By

from Pages.General import General

class OpenAccountPage(General):
    url = 'https://parabank.parasoft.com/parabank/openaccount.htm'

    # ID and ClassName List
    openAccountTitleCssSelector = 'div h1.title'
    openAccountButtonCssSelector = "input[value='Open New Account']"

    openAccountText = 'Open New Account'

    def __init__(self, driver):
        super(OpenAccountPage, self).__init__(driver=driver)

    def open_new_account_page(self):
        self.driver.find_element(By.LINK_TEXT, self.openAccountText).click()
        return self.is_page(self.URL, self.openAccountText)

    def create_new_account(self):
        print (self.driver.find_element(By.CSS_SELECTOR, self.openAccountButtonCssSelector))
        self.driver.find_element(By.CSS_SELECTOR, self.openAccountButtonCssSelector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.openAccountButtonCssSelector).click()