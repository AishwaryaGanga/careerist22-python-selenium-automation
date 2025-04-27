from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page_opened(context):
    context.app.terms_and_conditions_page.verify_terms_and_conditions_page_opened()

@then('User can close new window and switch back to original')
def close_page(context):
    context.app.base_page.close_page()
    context.app.base_page.switch_to_window_by_id(context.orginal_window)