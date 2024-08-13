from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class AddProjectPage(BasePage):
    NAME_INPUT = (By.CSS_SELECTOR, 'input#Your-name')
    COM_NAME_INPUT = (By.CSS_SELECTOR, 'input#Your-company-name')
    ROLE_INPUT = (By.CSS_SELECTOR, 'input#Role')
    AGE_INPUT = (By.CSS_SELECTOR, 'input#Age-of-the-company')
    COUNTRY_INPUT = (By.CSS_SELECTOR, 'input#Country')
    PROJ_NAME_INPUT = (By.CSS_SELECTOR, 'input#Name-project')
    PHONE_INPUT = (By.CSS_SELECTOR, 'input#Phone')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input#Email-add-project')
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

    def input_role_name(self, name):
        input_com_name = self.find_element(*self.ROLE_INPUT)
        input_com_name.clear()
        #self.clear()
        self.input_text(name, *self.ROLE_INPUT)
        sleep(2)

    def input_age(self, age):
        input_com_name = self.find_element(*self.AGE_INPUT)
        input_com_name.clear()
        #self.clear()
        self.input_text(age, *self.AGE_INPUT)
        sleep(2)

    def input_country(self, name):
        input_com_name = self.find_element(*self.COUNTRY_INPUT)
        input_com_name.clear()
        #self.clear()
        self.input_text(name, *self.COUNTRY_INPUT)
        sleep(2)

    def input_project_name(self, name):
        input_proj_name = self.find_element(*self.PROJ_NAME_INPUT)
        input_proj_name.clear()
        #self.clear()
        self.input_text(name, *self.PROJ_NAME_INPUT)
        sleep(2)

    def input_phone_num(self, num):
        input_proj_name = self.find_element(*self.PHONE_INPUT)
        input_proj_name.clear()
        #self.clear()
        self.input_text(num, *self.PHONE_INPUT)
        sleep(2)

    def input_email(self, email):
        input_proj_name = self.find_element(*self.EMAIL_INPUT)
        input_proj_name.clear()
        #self.clear()
        self.input_text(email, *self.EMAIL_INPUT)
        sleep(2)

    def verify_name(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#Your-name').get_attribute('value')
        expected_result = 'Daenerys'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_com_name(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#Your-company-name').get_attribute('value')
        expected_result = 'Krispy Kreme'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_com_role(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#Role').get_attribute('value')
        expected_result = 'QA'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_com_age(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#Age-of-the-company').get_attribute('value')
        expected_result = '1'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_country(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#Country').get_attribute('value')
        expected_result = 'USA'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_proj_name(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#Name-project').get_attribute('value')
        expected_result = 'Venti Towers'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_phone_num(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#Phone').get_attribute('value')
        expected_result = '1 800 789 2345'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_email(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input#Email-add-project').get_attribute('value')
        expected_result = 'venti_towersUSA@gmail.com'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_app_btn(self):
        send_app_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEND_APP_BTN)
        )
        assert send_app_button.is_displayed(), "Send application button is not available"
        assert send_app_button.is_enabled(), "Send application button is not clickable"
        # tooltip = self.find_element(*self.TOOLTIP_TEXT)
        #
        # actions = ActionChains(self.driver)
        # actions.move_to_element(tooltip).perform()
        # sleep(8)
        #
        # self.verify_text('Please fill out this field', *self.TOOLTIP_TEXT)