from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Verify that the Community page opens')
def verify_comm_page(context):
    context.app.community_page.verify_comm_page()

@then('Click the “Contact support” button is available and clickable')
def verify_supp_btn(context):
    context.app.community_page.verify_supp_btn()