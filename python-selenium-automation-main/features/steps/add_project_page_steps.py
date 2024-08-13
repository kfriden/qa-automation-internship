from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Enter test data into the name field: {name}')
def input_name(context, name):
    context.app.add_project_page.input_name(name)

@when('Enter test data into the Company name field: {name}')
def input_company_name(context, name):
    context.app.add_project_page.input_company_name(name)

@when('Enter test data into the Company role field: {name}')
def input_role_name(context, name):
    context.app.add_project_page.input_role_name(name)

@when('Enter test data into the age of company field: {age}')
def input_age(context, age):
    context.app.add_project_page.input_age(age)

@when('Enter test data into the country of project field: {name}')
def input_country(context, name):
    context.app.add_project_page.input_country(name)

@when('Enter test data into the Name of project field: {name}')
def input_project_name(context, name):
    context.app.add_project_page.input_project_name(name)

@when('Enter test data into the phone number field: {num}')
def input_phone_num(context, num):
    context.app.add_project_page.input_phone_num(num)

@when('Enter test data into the email field: {email}')
def input_email(context, email):
    context.app.add_project_page.input_email(email)

@then('Verify the right information is present in the name field')
def verify_name(context):
    context.app.add_project_page.verify_name()

@then('Verify the right information is present in the Company name field')
def verify_com_name(context):
    context.app.add_project_page.verify_com_name()

@then('Verify the right information is present in the Company role field')
def verify_com_role(context):
    context.app.add_project_page.verify_com_role()

@then('Verify the right information is present in the Company age field')
def verify_com_age(context):
    context.app.add_project_page.verify_com_age()

@then('Verify the right information is present in the Company country field')
def verify_country(context):
    context.app.add_project_page.verify_country()

@then('Verify the right information is present in the Name of project field')
def verify_proj_name(context):
    context.app.add_project_page.verify_proj_name()

@then('Verify the right information is present in the phone number field')
def verify_phone_num(context):
    context.app.add_project_page.verify_phone_num()

@then('Verify the right information is present in the email field')
def verify_email(context):
    context.app.add_project_page.verify_email()

@when('Click "Send an application" button below')
def click_app_btn(context):
    context.app.add_project_page.click_app_btn()

@when('Verify "Send an application" button is available and clickable')
def verify_app_btn(context):
    context.app.add_project_page.verify_app_btn()