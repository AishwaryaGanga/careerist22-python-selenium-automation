from selenium.webdriver.common.by import By
from Pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN = (By.CSS_SELECTOR, ".sc-43f80224-3")
    NAV_SIGN_IN = (By.CSS_SELECTOR, "[data-test = 'accountNav-signIn']")



    def search(self, text):
        print(f'Searching for {text}')
        self.input_text(text, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def click_sign_in(self):
        self.click(*self.SIGN_IN)

    def click_nav_sign_in(self):
        self.click(*self.NAV_SIGN_IN)