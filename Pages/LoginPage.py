from selenium.webdriver.common.by import By

from Pages.General import General

class LoginPage(General):

    #ID and ClassName List
    usernameTextBoxNAME = 'username'
    passwordTextBoxName = 'password'
    loginInButtonCssSelector = 'input[value="Log In"]'

    #Strings to use at tests
    user = 'cesarSchool123'
    password = '123456'

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.open_page()

    def open_page(self):
        self.driver.get(self.url)

    def login(self):
        self.driver.find_element(By.NAME, self.usernameTextBoxNAME).send_keys(self.user)
        self.driver.find_element(By.NAME, self.passwordTextBoxName).send_keys(self.password)
        self.click_login_button()

    def click_login_button(self):
        login_btn = self.driver.find_element(By.CSS_SELECTOR, self.loginInButtonCssSelector)
        login_btn.click()
