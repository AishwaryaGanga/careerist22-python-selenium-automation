from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultPage(Page):

    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    CART_BUTTON = (By.CSS_SELECTOR, "[data-test = '@web/CartLink']")
    VIEW_CART = (By.CSS_SELECTOR, "a[class *='styles_ndsBaseButton']")
    ADD_TO_CART = (By.CSS_SELECTOR, "[ data-test = 'orderPickupButton']")
    CLICK_MUG = (By.CSS_SELECTOR, "[id *= 'addToCartButtonOrTextIdFor91915654']")

    def verify_search_results(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT)

    def verify_results_url(self, expected_partial_url):
            self.verify_partial_url(expected_partial_url)

    def click_the_cart(self):
        self.wait.until(EC.element_to_be_clickable(*self.CART_BUTTON)).click()

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_MUG)).click()
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART)).click()
        self.wait.until(EC.element_to_be_clickable(self.VIEW_CART)).click()

