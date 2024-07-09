from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify that the correct tab opens')
def verify_cc_opened(context):
    context.app.connect_the_company_page.verify_cc_opened()

@when('Switch to current window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()