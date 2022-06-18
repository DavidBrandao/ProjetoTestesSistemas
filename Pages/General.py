from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class General:
    url = "https://parabank.parasoft.com/parabank/index.htm"

    titleCssSelector = 'div h1.title'

    def __init__(self, browser=None, driver=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                chrome_driver = Service(executable_path=ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=chrome_driver)
            elif browser == 'firefox':
                firefox_driver = Service(executable_path=GeckoDriverManager().install())
                self.driver = webdriver.Firefox(service=firefox_driver)
            else:
                raise Exception('Browser não suportado!')

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def quit_driver(self):
        self.driver.quit()

    def is_page(self, url, title=None):
        is_url = self.driver.current_url == url

        if title:
            element_title = self.driver.find_element(By.CSS_SELECTOR, self.titleCssSelector)
            is_title = element_title.text == title
            return is_url and is_title
        else:
            return is_url

