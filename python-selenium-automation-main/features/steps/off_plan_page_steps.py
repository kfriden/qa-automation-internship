from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on off plan at the left side menu')
def click_off_plan(context):
    context.app.off_plan_page.click_off_plan()

@when('Verify the off plan page opens')
def verify_off_plan(context):
    context.app.off_plan_page.verify_off_plan()

@then('Verify the price in all cards is inside the range ({min_price} - {max_price})')
def verify_prices_in_range(context, min_price, max_price):
    sleep(5)
    context.app.off_plan_page.verify_price_range(min_price, max_price)

@then('Click filter button in top left-hand corner')
def click_filter_button(context):
    context.app.off_plan_page.click_filter_button()

@then('Input unit price from {price} AED')
def input_unit_price_from(context, price):
    context.app.off_plan_page.input_unit_price_from(price)

@then('Input unit price to {price} AED')
def input_unit_price_from(context, price):
    context.app.off_plan_page.input_unit_price_to(price)

@when('Click Apply filter button')
def click_apply_filter(context):
    context.app.off_plan_page.click_apply_filter()

# MOBILE STEPS

@when('Click on off plan at the bottom left')
def click_off_plan_mobile(context):
    context.app.off_plan_page.click_off_plan_mobile()

@then('Click filter button in top right-hand corner')
def click_filter_button(context):
    context.app.off_plan_page.click_filter_button_mobile()