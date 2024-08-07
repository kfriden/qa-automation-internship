from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage
from pages.registration_page import RegistrationPage
from pages.connect_the_company_page import ConnectTheCompanyPage
from pages.settings_page import SettingsPage

class Application:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.registration_page = RegistrationPage(driver)
        self.connect_the_company_page = ConnectTheCompanyPage(driver)
        self.settings_page = SettingsPage(driver)

