from selenium.webdriver.common.by import By

from Pages.General import General


class MenuPage(General):

    sidebarbtnID = 'react-burger-menu-btn'
    logoutbtnID = 'logout_sidebar_link'
    itemListCN = 'bm-item-list'

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def open_menu_sidebar(self):
        self.driver.find_element(By.ID, self.sidebarbtnID).click()

    def click_logout_option(self):
        self.driver.find_element(By.ID, self.logoutbtnID).click()
