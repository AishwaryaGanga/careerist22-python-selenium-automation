from selenium.webdriver.common.by import By
from Pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_cart_empty(self):
        expected_result = "Your cart is empty"
        actual_result = self.find_element(*self.CART_EMPTY_MSG)
        assert actual_result.text == expected_result, f'Expected: {expected_result}, Actual: {actual_result.text}'

