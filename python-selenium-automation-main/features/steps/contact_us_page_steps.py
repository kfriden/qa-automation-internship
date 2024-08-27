from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify the correct page opens')
def verify_cont_page(context):
    context.app.contact_us_page.verify_cont_page()

@then('Verify there are at least 4 social media icons')
def verify_socials(context):
    context.app.contact_us_page.verify_socials()

@then('Verify “Connect the company” button is available and clickable')
def connect_comp_btn(context):
    context.app.contact_us_page.connect_comp_btn()