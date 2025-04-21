from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


PAGE_TEXT =  (By.CSS_SELECTOR, ".styles_fontSize1__i0fbt")
#ADD_TO_CART = (By.XPATH, "[data-test ='shippingButton']")
#practice purpose (By.XPATH, "//a[@data-test = '@web/CartLink']")

@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click on the Cart icon')
def click_the_cart(context):
    context.app.search_result_page.click_the_cart()

@when('Add the product to the cart')
def add_to_cart(context):
    context.app.search_result_page.add_to_cart()