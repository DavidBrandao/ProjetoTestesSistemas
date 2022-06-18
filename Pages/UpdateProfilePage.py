import random
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Pages.General import General


class UpdateProfilePage(General):
    url = 'https://parabank.parasoft.com/parabank/updateprofile.htm'

    # ID and ClassName List
    firstNameTextBoxID = 'customer.firstName'
    lastNameTextBoxID = 'customer.lastName'
    addressTextBoxID = 'customer.address.street'
    cityTextBoxID = 'customer.address.city'
    stateTextBoxID = 'customer.address.state'
    zipCodeTextBoxID = 'customer.address.zipCode'
    phoneNumberTextBoxID = 'customer.phoneNumber'

    titleCssSelector = 'div h1.title'
    messageSuccessCssSelector = 'div[ng-if="showResult"] p'

    menuText = 'Update Contact Info'
    titleText = 'Update Profile'
    messageSuccessText = 'Your updated address and phone number have been added to the system.'

    updateProfileButtonCssSelector = 'input[value="Update Profile"]'

    def __init__(self, driver):
        super(UpdateProfilePage, self).__init__(driver=driver)

    def open_update_profile_page(self):
        # Click update contact info button
        self.driver.find_element(By.LINK_TEXT, self.menuText).click()

        # Verify page URL
        is_url = self.driver.current_url == self.url

        # Get page title
        element_title = self.driver.find_element(By.CSS_SELECTOR, self.titleCssSelector)

        # Verify page title
        is_title = element_title.text == self.titleText
        return is_url and is_title

    def are_fields_visible(self):
        return (self.driver.find_element(By.NAME, self.firstNameTextBoxID).is_displayed() and
                self.driver.find_element(By.NAME, self.lastNameTextBoxID).is_displayed() and
                self.driver.find_element(By.NAME, self.addressTextBoxID).is_displayed() and
                self.driver.find_element(By.NAME, self.stateTextBoxID).is_displayed() and
                self.driver.find_element(By.NAME, self.zipCodeTextBoxID).is_displayed() and
                self.driver.find_element(By.NAME, self.phoneNumberTextBoxID).is_displayed())

    def edit_zipCode_text_box(self):
        self.edit_text_box_empty(self.zipCodeTextBoxID)
        num = random.randint(1000000, 9000000)
        self.driver.find_element(By.NAME, self.zipCodeTextBoxID).send_keys(num)
        self.click_update_profile_button()
        return num

    def edit_text_box_empty(self, element):
        self.driver.find_element(By.NAME, element).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(By.NAME, element).send_keys(Keys.DELETE)

    def click_update_profile_button(self):
        login_btn = self.driver.find_element(By.CSS_SELECTOR, self.updateProfileButtonCssSelector)
        login_btn.click()

    def verify_success_message_is_displayed(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, self.messageSuccessCssSelector)))
        return self.driver.find_element(By.CSS_SELECTOR, self.messageSuccessCssSelector).is_displayed()

    def verify_update_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.messageSuccessCssSelector).text == self.messageSuccessText

    def check_ZipCode_change(self, changeZipCodeText):
        time.sleep(2)
        return self.driver.find_element(By.NAME, self.zipCodeTextBoxID).get_attribute('value') == str(changeZipCodeText)
