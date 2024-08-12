from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class AddProjectPage(BasePage):
    NAME_INPUT = (By.CSS_SELECTOR, 'input#Your-name')
    COM_NAME_INPUT = (By.CSS_SELECTOR, 'input#Your-company-name')
    PROJ_NAME_INPUT = (By.CSS_SELECTOR, 'input#Name-project')
    SEND_APP_BTN = (By.CSS_SELECTOR, 'input[class="purchase-access w-button"]')
    TOOLTIP_TEXT = (By.XPATH, "//*[text()='Please fill out this field']")


    def input_name(self, name):
        input_fname = self.find_element(*self.NAME_INPUT)
        input_fname.clear()
        #self.clear()
        self.input_text(name, *self.NAME_INPUT)
        sleep(2)

    def input_company_name(self, name):
        input_com_name = self.find_element(*self.COM_NAME_INPUT)
        input_com_name.clear()
        #self.clear()
        self.input_text(name, *self.COM_NAME_INPUT)
        sleep(2)

    def input_project_name(self, name):
        input_proj_name = self.find_element(*self.PROJ_NAME_INPUT)
        input_proj_name.clear()
        #self.clear()
        self.input_text(name, *self.PROJ_NAME_INPUT)
        sleep(2)

    def verify_name(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#Your-name').get_attribute('value')
        expected_result = 'Daenerys'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_com_name(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#Your-company-name').get_attribute('value')
        expected_result = 'Krispy Kreme'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_proj_name(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#Name-project').get_attribute('value')
        expected_result = 'Venti Towers'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def click_app_btn(self):
        self.click(*self.SEND_APP_BTN)
        sleep(2)

    def verify_app_btn(self):
        tooltip = self.find_element(*self.TOOLTIP_TEXT)

        actions = ActionChains(self.driver)
        actions.move_to_element(tooltip).perform()
        sleep(8)

        self.verify_text('Please fill out this field', *self.TOOLTIP_TEXT)