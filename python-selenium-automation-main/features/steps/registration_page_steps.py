from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open registration page')
def open_registration(context):
    context.app.registration_page.open_registration()

@then('Input text for first and last name {fullname}')
def input_username(context, fullname):
    context.app.registration_page.input_name(fullname)

@then('Input text for phone {phone}')
def input_phone(context, phone):
    context.app.registration_page.input_phone(phone)

@then('Input text for password {password}')
def input_phone(context, password):
    context.app.registration_page.input_password(password)

@when('Input text for email {email}')
def input_email(context, email):
    context.app.registration_page.input_email(email)

@when('Verify info in first and last name field')
def verify_name(context):
    context.app.registration_page.verify_name()

@then('Verify info in phone number field')
def verify_phone(context):
    context.app.registration_page.verify_phone()

@then('Verify info in email field')
def verify_email(context):
    context.app.registration_page.verify_email()

@then('Verify info in password field')
def verify_password(context):
    context.app.registration_page.verify_password()