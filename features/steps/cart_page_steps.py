from selenium.webdriver.common.by import By
from behave import given, when, then


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()

@then("Verify cart page opens")
def verify_cart_page_opens(context):
    context.app.cart_page.verify_cart_page_opens()

@then("Verify cart has the product")
def verify_cart_has_product(context):
    context.app.cart_page.verify_cart_has_product()