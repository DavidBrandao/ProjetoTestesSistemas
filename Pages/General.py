from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class General:

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


    def QuitDriver(self):
        self.driver.quit()
