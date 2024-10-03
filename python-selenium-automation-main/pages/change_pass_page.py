from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ChangePassPage(BasePage):
    NEW_PASS_INPUT = (By.CSS_SELECTOR, 'input[name="Enter-new-password"]')
    REPEAT_PASS_INPUT = (By.CSS_SELECTOR, 'input[name="Repeat-password"]')
    CHANGE_PASS_BTN = (By.CSS_SELECTOR, "a[wized='changePasswordButton']")

    def verify_change_pass_page(self):
        self.verify_partial_url('/set-new-password')

    def input_new_pass(self, password):
        self.click(*self.NEW_PASS_INPUT)
        self.input_text(password, *self.NEW_PASS_INPUT)
        sleep(2)

    def repeat_new_pass(self, password):
        self.click(*self.REPEAT_PASS_INPUT)
        self.input_text(password, *self.REPEAT_PASS_INPUT)
        sleep(2)

    def verify_change_pass_btn(self):
        change_pass_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CHANGE_PASS_BTN)
        )
        assert change_pass_btn.is_displayed(), "change password button is not available"