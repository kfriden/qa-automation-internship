from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class ConnectTheCompanyPage(BasePage):

    def verify_cc_opened(self):
        self.verify_partial_url('book-presentation')