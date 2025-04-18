from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify Sign in form opened')
def verify_sign_in_page_opens(context):
    context.app.sign_in_page.verify_sign_in_page_opens()

@then('Verify user can login')
def verify_user_logins(context):
   context.app.header.input_email()
   context.app.header.input_password()