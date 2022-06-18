from selenium.webdriver.common.by import By

from Pages.General import General


class ProductsPage(General):
    txtProducts = 'PRODUCTS'
    titleCN = 'title'
    addBackpackID = 'add-to-cart-sauce-labs-backpack'
    removeBackpackID = 'remove-sauce-labs-backpack'

    itemListCN = 'inventory_item'
    primaryBtnCN = 'btn_primary'

    def add_first_product(self):
        element_list = self.driver.find_elements(By.CLASS_NAME, self.itemListCN)
        element_list[0].find_element(By.CLASS_NAME, self.primaryBtnCN).click()

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver = driver)

    def get_page_tile_after_login(self):
        return self.driver.find_element(By.CLASS_NAME, self.titleCN).text

    def add_backpack_to_cart(self):
        self.driver.find_element(By.ID, self.addBackpackID).click()

    def verify_backpack_remove_btn_visible(self):
        return self.driver.find_element(By.ID, self.removeBackpackID).is_displayed()

    # New method
    def is_products_page(self):
        return self.is_page(self.url, title=self.txtProducts)
