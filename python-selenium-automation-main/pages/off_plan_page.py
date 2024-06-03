from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class OffPlanPage(BasePage):
    OFF_PLAN_BTN = (By.XPATH, "//div[text()='Off-plan']")
    APPLY_FILTER_BTN = (By.XPATH, "//a[@wized='applyFilterButton']")
    FILTER_BTN = (By.CSS_SELECTOR, 'a[class="filter-button w-inline-block"]')
    UNIT_PRICE_FROM = (By.XPATH, "//input[@id='field-5' and @wized='unitPriceFromFilter']")
    UNIT_PRICE_TO = (By.XPATH, "//input[@id='field-5' and @wized='unitPriceToFilter']")
    PRICES = (By.CSS_SELECTOR, "[class='price-value']")

    def click_off_plan(self):
        self.wait_until_clickable(*self.OFF_PLAN_BTN)
        # self.click(*self.OFF_PLAN_BTN)
        sleep(6)

    def click_filter_button(self):
        self.click(*self.FILTER_BTN)
        sleep(3)

    def click_apply_filter(self):
        self.click(*self.APPLY_FILTER_BTN)
        sleep(3)

    def input_unit_price_from(self, price):
        self.click(*self.UNIT_PRICE_FROM)
        self.input_text(price, *self.UNIT_PRICE_FROM)
        sleep(2)

    def input_unit_price_to(self, price):
        self.click(*self.UNIT_PRICE_TO)
        self.input_text(price, *self.UNIT_PRICE_TO)
        sleep(8)

    def verify_off_plan(self):
        actual_text = self.driver.find_element(By.XPATH, "//div[text()='Total projects']").text
        assert 'Total projects' in actual_text, f'Error: Text not in {actual_text}'

    def verify_price_range(self, min_price, max_price):
        product_prices = self.driver.find_elements(*self.PRICES)
        min_price = int(min_price)
        max_price = int(max_price)

        for price_element in product_prices:
            price = int(price_element.text.replace("AED", "").replace(",", "").strip())
            assert min_price <= price <= max_price, f"Price {price} is not in the expected range."



