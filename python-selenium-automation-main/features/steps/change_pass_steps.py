from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify that the change password page opens')
def verify_change_pass_page(context):
    context.app.change_pass_page.verify_change_pass_page()

@then('Add text in Enter new password input field {password}')
def input_new_pass(context, password):
    context.app.change_pass_page.input_new_pass(password)

@then('Re-enter password in repeat password input field {password}')
def repeat_new_pass(context, password):
    context.app.change_pass_page.repeat_new_pass(password)

@when('Verify the “Change password” button is available')
def verify_change_pass_btn(context):
    context.app.change_pass_page.verify_change_pass_btn()