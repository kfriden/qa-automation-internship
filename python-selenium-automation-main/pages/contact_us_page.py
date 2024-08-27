from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class ContactUsPage(BasePage):
    SOCIAL_BTNS = (By.CLASS_NAME, "social-button")
    CONNECT_COMP_BTN = (By.CSS_SELECTOR, "#w-node-c6d488e5-136e-84a4-dfe5-316eac5e5682-7f66debb")


    def verify_cont_page(self):
        self.verify_partial_url('/contact-us')

    def verify_socials(self):
        print(self.find_elements(*self.SOCIAL_BTNS))

    def connect_comp_btn(self):
        connect_comp_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONNECT_COMP_BTN)
        )
        assert connect_comp_btn.is_displayed(), "connect_comp button is not available"
        assert connect_comp_btn.is_enabled(), "connect_comp button is not clickable"