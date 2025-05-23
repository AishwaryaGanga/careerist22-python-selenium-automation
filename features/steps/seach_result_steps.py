from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


@when('Click on Add to Cart button')
def side_nav_click_add_to_cart(context):
    pass

@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    context.app.search_result_page.verify_search_results(expected_text)

@then('Verify {expected_text} in URL')
def verify_results_url(context, expected_text):
    context.app.search_result_page.verify_results_url(expected_text)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(2)
    # context.driver.execute_script("window.scrollBy(0,1000)", "")
    # sleep(2)

    products = context.driver.find_elements(*LISTINGS)[:8]  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)
