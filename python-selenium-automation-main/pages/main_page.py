from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep



class MainPage(BasePage):
    USERNAME_INPUT = (By.ID, 'email-2')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'a[class*="login-button"]')

    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def input_username(self, username):
        self.click(*self.USERNAME_INPUT)
        self.input_text(username, *self.USERNAME_INPUT)
        sleep(2)

    def input_password(self, password):
        self.click(*self.PASSWORD_INPUT)
        self.input_text(password, *self.PASSWORD_INPUT)
        sleep(2)

    def click_continue(self):
        self.click(*self.LOGIN_BTN)
        sleep(2)