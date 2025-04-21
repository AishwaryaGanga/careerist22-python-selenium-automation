from selenium.webdriver.common.by import By
from Pages.base_page import Page




class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    ACTUAL_TEXT = (By.CSS_SELECTOR, ("div[class='styles_ndsTruncate__GRSDE h-text-bs'] div"))

    def verify_cart_empty(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_cart_page_opens(self):
        #self.verify_url('https://www.target.com/cart')
        self.verify_url(f'{self.base_url}cart')  # 'https://www.target.com/' + 'cart'

    def verify_cart_has_product(self):
        expected_text = "16oz Stoneware Love You Mom Mug Blue - Room Essentials"
        actual_text = self.find_element(*self.ACTUAL_TEXT).text
        assert expected_text in actual_text, f'Expected text {expected_text} did not match actual {actual_text}'



