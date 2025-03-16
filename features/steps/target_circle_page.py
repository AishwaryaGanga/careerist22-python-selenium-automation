from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

LINKS = (By.CSS_SELECTOR, "[data-test = '@web/slingshot-components/CellsComponent/Link']")

@given('Open target circle page')
def open_target_cirle_page(context):
    context.driver.get("https://www.target.com/l/target-circle/-/N-pzno9")

@then('Verify 15 benefit cells')
def verify_benefits(context):
    links = context.driver.find_elements(*LINKS)
    assert len(links) == 15, f'Expected 10 links, but got {len(links)}'
    print(links)