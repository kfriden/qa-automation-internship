from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(BasePage):
    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in')