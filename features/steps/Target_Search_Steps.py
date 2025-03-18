from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


CART_BUTTON = (By.CSS_SELECTOR,"[data-test = '@web/CartLink']")
PAGE_TEXT =  (By.CSS_SELECTOR, ".styles_fontSize1__i0fbt")
CLICK_CHOCOLATE = (By.CSS_SELECTOR, "[title *= 'Lindt Lindor White Chocolate Candy Truffles']")
#ADD_TO_CART = (By.XPATH, "[data-test ='shippingButton']")
ADD_TO_CART = (By.XPATH, "//div[@class='sc-c0a4129a-0 iwjIfA']//div//button[@id='addToCartButtonOrTextIdFor12943084']")
#practice purpose (By.XPATH, "//a[@data-test = '@web/CartLink']")
VIEW_CART = (By.CSS_SELECTOR, "a[href='/cart']")

@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click on the Cart icon')
def input_search(context):
    context.driver.find_element(*CART_BUTTON).click()
    sleep(3)

@when('Add the product to the cart')
def add_to_cart(context):
    context.driver.find_element(*CLICK_CHOCOLATE).click()
    sleep(10)
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(10)
    context.driver.find_element(*VIEW_CART).click()
    sleep(10)
