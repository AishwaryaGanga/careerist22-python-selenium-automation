from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



#from sample_script import driver

CART_BUTTON = (By.CSS_SELECTOR,"[data-test = '@web/CartLink']")
PAGE_TEXT =  (By.CSS_SELECTOR, ".styles_fontSize1__i0fbt")

#practice purpose (By.XPATH, "//a[@data-test = '@web/CartLink']")

@given('Open target.com')
def open_google(context):
    context.driver.get('https://www.target.com/')


@when('Click on the Cart icon')
def input_search(context):
    cart = context.driver.find_element(*CART_BUTTON).click()
    sleep(3)

@then('Verify "Your cart is empty"')
def verify_empty(context):
    page_text_element = context.driver.find_element(*PAGE_TEXT)
    assert "Your cart is empty" in page_text_element.text, \
        f'Expected text "Your cart is empty" not found in {page_text_element.text}'
