from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage
from pages.registration_page import RegistrationPage
from pages.connect_the_company_page import ConnectTheCompanyPage
from pages.settings_page import SettingsPage
from pages.add_project_page import AddProjectPage
from pages.community_page import CommunityPage
from pages.contact_us_page import ContactUsPage
from pages.user_guide_page import UserGuidePage
from pages.change_pass_page import ChangePassPage

class Application:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.registration_page = RegistrationPage(driver)
        self.connect_the_company_page = ConnectTheCompanyPage(driver)
        self.settings_page = SettingsPage(driver)
        self.add_project_page = AddProjectPage(driver)
        self.community_page = CommunityPage(driver)
        self.contact_us_page = ContactUsPage(driver)
        self.user_guide_page = UserGuidePage(driver)
        self.change_pass_page = ChangePassPage(driver)

