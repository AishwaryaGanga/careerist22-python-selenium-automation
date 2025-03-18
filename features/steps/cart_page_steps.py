from selenium.webdriver.common.by import By
from behave import given, when, then


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'

@then("Verify cart has the product")
def verify_cart_has_product(context):
    expected_result = '$5.99'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div[class *='styles_mdHiddenDown__MPUqz'] div[class='styles_ndsRow__iT6yG'] div div p[class *='sc-e6296628-0']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'

