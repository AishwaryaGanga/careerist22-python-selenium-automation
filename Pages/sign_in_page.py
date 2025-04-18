from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep

class SignInPage(Page):
    #SIGN_IN_TEXT = (By.CSS_SELECTOR, ".styles_ndsHeading__HcGpD")
    EMAIL = (By.ID, 'username')
    CONTINUE = (By.ID, 'continue')
    PASSWORD = (By.ID, 'password')
    LOGIN = (By.ID, 'login')

    def verify_sign_in_page_opens(self):
        self.verify_partial_url('https://www.target.com/login?')

    def input_email(self):
        self.input_text(self.EMAIL, 'stefano@gfacc.net')
        self.click(self.CONTINUE)

    def input_password(self):
        self.input_text(self.PASSWORD, 'Asdfghjkl')
        self.click(self.LOGIN)








