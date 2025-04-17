from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from app import application
from selenium.webdriver.support import expected_conditions as EC

SEARCH_FIELD = (By.ID, 'search')

HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")
ADD_CART = (By.XPATH, "[data-test ='shippingButton']")

@given('Open target main page')
def open_target_main(context):
    context.app.main_page.open_main_page()
    context.driver.wait.until(EC.presence_of_element_located(SEARCH_FIELD))


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search(search_word)


@when('Click on Cart icon')
def click_cart(context):
    #context.driver.find_element(*CART_ICON).click()
    context.app.header.click_cart()


@then('Verify at least 1 link shown')
def verify_1_header_link_shown(context):
    link = context.driver.wait.until(EC.presence_of_element_located(HEADER_LINKS))
    print(link)


@then('Verify {link_amount} links shown')
def verify_all_header_links_shown(context, link_amount):
    link_amount = int(link_amount) # "6" => int 6
    links = context.driver.wait.until(EC.presence_of_all_elements_located(HEADER_LINKS))
    print(links)
    assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}'


