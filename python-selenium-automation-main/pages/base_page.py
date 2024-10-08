from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def clear(self, *locator):
        self.driver.find_element(*locator).clear()

    def wait_until_clickable(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator), message=f'Element not clickable by {locator}').click()

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url), message= f'URL does not contain {expected_partial_url}')

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text}, but got {actual_text}'

    def save_screenshot(self, name):
        self.driver.save_screenshot(f'{name}.png')

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('ALL windows', self.driver.window_handles)
        print('Switching to...', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        print('Switching to...', window_id)
        self.driver.switch_to.window(window_id)
