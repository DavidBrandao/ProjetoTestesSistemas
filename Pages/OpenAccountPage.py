from selenium.webdriver.common.by import By

from Pages.General import General


class OpenAccountPage(General):

    # ID and ClassName List
    openAccountTitleCssSelector = 'div h1.title'
    openAccountButtonCssSelector = "input[value='Open New Account']"

    openAccountText = 'Open New Account'


    # Strings to use at tests
    user = 'cesarSchool123'
    password = '123456'

    def __init__(self, driver):
        super(OpenAccountPage, self).__init__(driver=driver)

    def open_new_account_page(self):
        self.driver.find_element(By.LINK_TEXT, self.openAccountText).click()
        return self.driver.find_element(By.CSS_SELECTOR, self.openAccountTitleCssSelector).text == self.openAccountText


    def create_new_account(self):
        print (self.driver.find_element(By.CSS_SELECTOR, self.openAccountButtonCssSelector))