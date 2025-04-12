from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


LINKS = (By.CSS_SELECTOR, ".container.clearfix")

@given("Open target help page")
def help_pg(context):
    context.driver.get("https://help.target.com/help")
    sleep(5)

@then("Verify the {link_count} links")
def verify_links(context, link_count):
    link_count = int(link_count)
    links = context.driver.find_elements(*LINKS)
    print(links)
    assert len(links) == link_count,f'Expected {link_count} links, but got {len(links)}'