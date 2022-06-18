import time
import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Pages.General import General

class UpdateProfilePage(General):
    url = 'https://parabank.parasoft.com/parabank/updateprofile.htm'

    #ID and ClassName List
    firstNameTextBoxID = 'customer.firstName'
    lastNameTextBoxID = 'customer.lastName'
    addressTextBoxID = 'customer.address.street'
    cityTextBoxID = 'customer.address.city'
    stateTextBoxID = 'customer.address.state'
    zipCodeTextBoxID = 'customer.address.zipCode'
    phoneNumberTextBoxID = 'customer.phoneNumber'

    messageSuccessCssSelector = 'div[ng-if="showResult"] p'

    menuText = 'Update Contact Info'
    titleText = 'Update Profile'
    messageSuccessText = 'Your updated address and phone number have been added to the system.'

    updateProfileButtonCssSelector = 'input[value="Update Profile"]'

    def __init__(self, driver):
        super(UpdateProfilePage, self).__init__(driver=driver)

    def is_url_update_profile(self):
        return self.driver.current_url == self.url_update_profile

    def open_update_profile_page(self):
        self.click_update_profile_menu()
        return self.is_page(self.url, self.titleText)

    def click_update_profile_menu(self):
        menu_update = self.driver.find_element(By.LINK_TEXT, self.menuText)
        menu_update.click()

    def are_fields_profile_page(self):
        return (self.driver.find_element(By.NAME, self.firstNameTextBoxID) and
                self.driver.find_element(By.NAME, self.lastNameTextBoxID) and
                self.driver.find_element(By.NAME, self.addressTextBoxID) and
                self.driver.find_element(By.NAME, self.stateTextBoxID) and
                self.driver.find_element(By.NAME, self.zipCodeTextBoxID) and
                self.driver.find_element(By.NAME, self.phoneNumberTextBoxID) and
                self.driver.find_element(By.NAME, self.phoneNumberTextBoxID))

    def edit_zipCode_text_box(self):
        self.edit_text_box_empety(self.zipCodeTextBoxID)
        num = random.randint(1000000, 9000000)
        self.driver.find_element(By.NAME, self.zipCodeTextBoxID).send_keys(num)
        self.click_update_profile_button()
        return num

    def edit_text_box_empety(self, element):
        self.driver.find_element(By.NAME, element).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(By.NAME, element).send_keys(Keys.DELETE)

    def click_update_profile_button(self):
        login_btn = self.driver.find_element(By.CSS_SELECTOR, self.updateProfileButtonCssSelector)
        login_btn.click()

    def presence_success_mens_until(self):
        time.sleep(2)
        return self.driver.find_element(By.CSS_SELECTOR, self.messageSuccessCssSelector)

    def has_update_message_success(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.messageSuccessCssSelector).text == self.messageSuccessText

    def check_ZipCode_change(self, changeZipCodeText):
        time.sleep(3)
        return self.driver.find_element(By.NAME, self.zipCodeTextBoxID).get_attribute('value') == str(changeZipCodeText)