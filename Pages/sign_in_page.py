from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep

class SignInPage(Page):
    #SIGN_IN_TEXT = (By.CSS_SELECTOR, ".styles_ndsHeading__HcGpD")

    def verify_sign_in_page_opens(self):
        self.verify_partial_url('https://www.target.com/login?')








