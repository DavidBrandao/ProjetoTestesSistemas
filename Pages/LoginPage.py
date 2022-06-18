from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Pages.General import General


class LoginPage(General):
    #Website URL
    url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'

    #ID and ClassName List
    userEmailTextBoxID = 'email'
    passwordTextBoxID = 'passwd'
    signInButtonID = 'SubmitLogin'

    #Strings to use at tests
    user = 'dfb@cesar.school.com'
    password = '123456'

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)

    def open_login_page(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def login(self):
        self.driver.find_element(By.ID, self.userEmailTextBoxID).send_keys(self.user)
        self.driver.find_element(By.ID, self.passwordTextBoxID).send_keys(self.password)
        self.click_login_button()

    def click_login_button(self):
        login_btn = self.driver.find_element(By.ID, self.signInButtonID)
        login_btn.click()

    def is_login_button_visible(self):
        return self.driver.find_element(By.ID, self.loginButtonID).is_displayed()