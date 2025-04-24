from selenium.webdriver.common.by import By
from behave import given, when, then

@given("Open target sign in page")
def click_login_page(context):
    context.app.sign_in_page.click_login_page()
    context.app.sign_in_page.input_email()


@given("Store original window")
def store_original_window(context):
    context.app.sign_in_page.store_original_window()

@when("Click on Target terms and conditions link")
def click_terms_and_conditions(context):
    context.app.sign_in_page.click_terms_and_conditions()

@when("Switch to the newly opened window")
def switch_to_newly_opened_window(context):
    context.app.sign_in_page.switch_to_newly_opened_window()



@then('Verify Sign in form opened')
def verify_sign_in_page_opens(context):
    context.app.sign_in_page.verify_sign_in_page_opens()

@then('Verify user can login')
def verify_user_logins(context):
   context.app.sign_in_page.input_email()
   context.app.sign_in_page.input_password()

