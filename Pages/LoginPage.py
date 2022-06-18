from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Pages.General import General


class LoginPage(General):
    #Website URL
    url = 'https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC'

    #ID and ClassName List
    usernameTextBoxNAME = 'username'
    passwordTextBoxName = 'password'
    signInButtonXPATH = '//*[@id="loginPanel"]/form/div[3]/input'

    #Strings to use at tests
    user = 'cesarSchool'
    password = '123456'

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)

    def open_login_page(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def login(self):
        self.driver.find_element(By.NAME, self.usernameTextBoxNAME).send_keys(self.user)
        self.driver.find_element(By.NAME, self.passwordTextBoxName).send_keys(self.password)
        self.click_login_button()

    def click_login_button(self):
        login_btn = self.driver.find_element(By.XPATH, self.signInButtonXPATH)
        login_btn.click()

    def is_login_button_visible(self):
        return self.driver.find_element(By.ID, self.signInButtonXPATH).is_displayed()