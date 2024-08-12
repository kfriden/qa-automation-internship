from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SettingsPage(BasePage):
    SETTINGS_BTN = (By.XPATH, "//div[text()='Settings']")
    EDIT_BTN = (By.XPATH, "//div[text()='Edit profile']")
    TESTNAME_INPUT = (By.CSS_SELECTOR, 'input[name="Fullname"]')
    TESTNUM_INPUT = (By.CSS_SELECTOR, 'input#number')
    TESTCOM_INPUT = (By.CSS_SELECTOR, 'input#Company-name')
    CLOSE_BTN = (By.CSS_SELECTOR, 'a.close-button')
    SAVE_BTN = (By.CSS_SELECTOR, 'div.save-changes-button')
    LANG_BUTTON = (By.CSS_SELECTOR, 'div#w-dropdown-toggle-0')
    RU_BTN = (By.XPATH, "//a[text()='RU']")
    ADD_PROJ_BTN = (By.XPATH, "//div[text()='Add a project']")

    def click_settings_btn(self):
        self.click(*self.SETTINGS_BTN)
        sleep(3)

    def click_edit_profile_btn(self):
        self.click(*self.EDIT_BTN)
        sleep(3)

    def click_save_btn(self):
        self.click(*self.SAVE_BTN)
        sleep(3)

    def click_close_btn(self):
        self.click(*self.CLOSE_BTN)
        sleep(3)

    def click_add_proj(self):
        self.click(*self.ADD_PROJ_BTN)
        sleep(3)

    def input_name(self, name):
        input_fname = self.find_element(*self.TESTNAME_INPUT)
        input_fname.clear()
        #self.clear()
        self.input_text(name, *self.TESTNAME_INPUT)
        sleep(2)

    def input_number(self, number):
        input_number = self.find_element(*self.TESTNUM_INPUT)
        input_number.clear()
        #self.clear()
        self.input_text(number, *self.TESTNUM_INPUT)
        sleep(2)

    def input_company(self, test):
        input_company = self.find_element(*self.TESTCOM_INPUT)
        input_company.clear()
        #self.clear()
        self.input_text(test, *self.TESTCOM_INPUT)
        sleep(2)

    def change_lng(self):
        lang_button = self.find_element(*self.LANG_BUTTON)

        actions = ActionChains(self.driver)
        actions.move_to_element(lang_button).perform()
        sleep(3)
        self.click(*self.RU_BTN)
        sleep(3)

    def verify_add_proj(self):
        self.verify_partial_url('/add-a-project')

    def verify_new_name(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input[name="Fullname"]').get_attribute('value')
        expected_result = 'Kit'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_new_num(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#number').get_attribute('value')
        expected_result = '668 902 7880'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_new_company(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#Company-name').get_attribute('value')
        expected_result = 'helllooooo'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_lang_change(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, "div#w-dropdown-toggle-0").text
        expected_result = 'RU'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

