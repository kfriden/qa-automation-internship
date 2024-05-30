from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main(context):
    context.app.main_page.open_main()

@when('Login to the main page with username {username}')
def input_username(context, username):
    context.app.main_page.input_username(username)

@when('Login to the main page with password {password}')
def input_password(context, password):
    context.app.main_page.input_password(password)

@then('Click continue button')
def click_continue(context):
    context.app.main_page.click_continue()

