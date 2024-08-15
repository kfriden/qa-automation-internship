from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class CommunityPage(BasePage):
    SUPP_BTN = (By.CSS_SELECTOR, "a#w-node-f7ead340-ee2a-2b84-cdd5-5a35322aacbf-7f66deba")


    def verify_comm_page(self):
        self.verify_partial_url('/community')

    def verify_supp_btn(self):
        self.click(*self.SUPP_BTN)
        sleep(3)
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('ALL windows', self.driver.window_handles)
        print('Switching to...', all_windows[1])
        self.driver.switch_to.window(all_windows[1])
        sleep(3)
        self.verify_partial_url('/reelly_dubai_bot')
