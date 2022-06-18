from selenium.webdriver.common.by import By

from Pages.General import General

class AccountsOverviewPage(General):
    url = 'https://parabank.parasoft.com/parabank/overview.htm'

    #ID and ClassName List
    titleText = 'Accounts Overview'
    passwordTextBoxName = 'password'
    loginInButtonCssSelector = 'input[value="Log In"]'

    def __init__(self, driver):
        super(AccountsOverviewPage, self).__init__(driver=driver)

    def is_url_accounts_overview(self):
        return self.driver.current_url == self.url

    def is_title_accounts_overview(self):
        return self.is_page(self.url, self.titleText)

    def click_update_profile_button(self):
        login_btn = self.driver.find_element(By.CSS_SELECTOR, self.updateProfileButtonCssSelector)
        login_btn.click()