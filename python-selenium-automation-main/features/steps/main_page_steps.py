from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main(context):
    context.app.open_main_page()