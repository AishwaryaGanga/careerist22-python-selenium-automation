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
    expected_result = '$5.99'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div[class *='styles_mdHiddenDown__MPUqz'] div[class='styles_ndsRow__iT6yG'] div div p[class *='sc-e6296628-0']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'

