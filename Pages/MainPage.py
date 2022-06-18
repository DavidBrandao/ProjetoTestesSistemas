from selenium.webdriver.common.by import By

from Pages.General import General


class MainPage(General):

    signOutButtonCN = 'logout'
    topButtonCN = 'sf-with-ul'


    def __init__(self, driver):
        super(MainPage, self).__init__(driver=driver)

    def verifyUserIsLogged(self):
        return self.driver.find_element(By.CLASS_NAME, self.signOutButtonCN).is_displayed()

    def clickDressesButton(self):
        element_list = self.driver.find_elements(By.CLASS_NAME, self.topButtonCN)
        print(len(element_list))
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        for item in element_list:
            if item.get_attribute('title') == 'Dresses':
                item.click()
                break

        # element_list[1].click()
