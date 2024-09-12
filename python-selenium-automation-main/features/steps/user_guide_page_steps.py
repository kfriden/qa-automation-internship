from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify that the user guide page opens')
def verify_guide(context):
    context.app.user_guide_page.verify_guide()

@then('Verify all lesson videos have titles')
def verify_video_titles(context):
    context.app.user_guide_page.verify_video_titles()