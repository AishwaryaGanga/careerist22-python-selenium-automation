from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test = 'product-title']")
PRODUCT_IMAGE = (By.CSS_SELECTOR, "[data-test *= '@web/ProductCard/ProductCardImage/secondary']")
PROD_LISTINGS = (By.CSS_SELECTOR, "[data-test *= '@web/site-top-of-funnel']")

@then("Verify products has a product name and image")
def verify_name_image_products(context):

    products = context.driver.find_elements(*PROD_LISTINGS)[:3]

    for product in products:

        names = product.find_elements(*PRODUCT_NAME)
        assert names, 'Product name not found'
        print("Product names: ", names)

        product.find_element(*PRODUCT_IMAGE)


