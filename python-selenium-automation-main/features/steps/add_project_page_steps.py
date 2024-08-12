from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Enter test data into the name field: {name}')
def input_name(context, name):
    context.app.add_project_page.input_name(name)

@when('Enter test data into the Company name field: {name}')
def input_company_name(context, name):
    context.app.add_project_page.input_company_name(name)

@when('Enter test data into the Name of project field: {name}')
def input_project_name(context, name):
    context.app.add_project_page.input_project_name(name)

@then('Verify the right information is present in the name field')
def verify_name(context):
    context.app.add_project_page.verify_name()

@then('Verify the right information is present in the Company name field')
def verify_com_name(context):
    context.app.add_project_page.verify_com_name()

@then('Verify the right information is present in the Name of project field')
def verify_proj_name(context):
    context.app.add_project_page.verify_proj_name()

@when('Click "Send an application" button below')
def click_app_btn(context):
    context.app.add_project_page.click_app_btn()

@when('Verify "Send an application" button is available and clickable')
def verify_app_btn(context):
    context.app.add_project_page.verify_app_btn()