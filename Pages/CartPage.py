from selenium.webdriver.common.by import By

from Pages.General import General


class CartPage(General):

    cartButtonID = 'shopping_cart_container'
    checkoutButtonID = 'checkout'

    def __init__(self, driver):
        super(CartPage, self).__init__(driver=driver)

    def click_cart_button(self):
        self.driver.find_element(By.ID, self.cartButtonID).click()

    def click_checkout_button(self):
        self.driver.find_element(By.ID, self.checkoutButtonID).click()
