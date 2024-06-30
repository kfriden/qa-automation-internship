from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class RegistrationPage(BasePage):
    FULLNAME_INPUT = (By.CSS_SELECTOR, 'input[name="Full-Name"]')
    PHONE_INPUT = (By.CSS_SELECTOR, 'input[name="Phone"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="Email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="Password"]')


    def open_registration(self):
        self.driver.get('https://soft.reelly.io/sign-up')
        sleep(5)

    def input_name(self, fullname):
        self.click(*self.FULLNAME_INPUT)
        self.input_text(fullname, *self.FULLNAME_INPUT)
        sleep(2)

    def input_email(self, email):
        self.click(*self.EMAIL_INPUT)
        self.input_text(email, *self.EMAIL_INPUT)
        sleep(2)

    def input_password(self, password):
        self.click(*self.PASSWORD_INPUT)
        self.input_text(password, *self.PASSWORD_INPUT)
        sleep(2)

    def input_phone(self, phone):
        self.click(*self.PHONE_INPUT)
        self.input_text(phone, *self.PHONE_INPUT)
        sleep(2)

    def verify_name(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input[name="Full-Name"]').get_attribute('value')
        assert 'Kaitlyn Friden' in actual_text, f'Error: Text not in {actual_text}'

    def verify_phone(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input[name="Phone"]').get_attribute('value')
        assert '888 350 1600' in actual_text, f'Error: Text not in {actual_text}'

    def verify_email(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input[name="Email"]').get_attribute('value')
        assert 'cutelizzie@verizon.net' in actual_text, f'Error: Text not in {actual_text}'

    def verify_password(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input[name="Password"]').get_attribute('value')
        assert '$onicx89' in actual_text, f'Error: Text not in {actual_text}'