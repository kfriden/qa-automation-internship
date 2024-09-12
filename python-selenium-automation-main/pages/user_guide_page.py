from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class UserGuidePage(BasePage):
    VIDEO_TITLE = By.CSS_SELECTOR, "a[data-sessionlink='feature=player-title']"



    def verify_guide(self):
        self.verify_partial_url('/user-guide')

    def verify_video_titles(self):
        videos = self.find_elements(*self.VIDEO_TITLE)

        for video in videos:
            title = video.find_element(*self.VIDEO_TITLE).text
            assert title, 'Full overview of Reelly platform'
