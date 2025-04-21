from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep

class SignInPage(Page):
    #SIGN_IN_TEXT = (By.CSS_SELECTOR, ".styles_ndsHeading__HcGpD")
    EMAIL = (By.ID, 'username')
    CONTINUE = (By.ID, 'continue')
    PASSWORD = (By.ID, 'password')
    LOGIN = (By.ID, 'login')
    PRIVACY_POLICY = (By.CSS_SELECTOR,"[aria-label *= 'terms & conditions']" )


    def open_target_sign_in_page(self):
        self.open_url("https://mytargetcirclecard.target.com/ecs/auth/?cid=AAAA6331001")
        sleep(5)

    def store_original_window(self):
        self.current_window_handle = self.driver.current_window_handle
        print("Current window handle: ", self.current_window_handle)

    def click_terms_and_conditions(self):
        self.click(*self.PRIVACY_POLICY)

    def verify_sign_in_page_opens(self):
        self.verify_partial_url('https://www.target.com/login?')



    def input_email(self):
        self.input_text(self.EMAIL, 'stefano@gfacc.net')
        self.click(self.CONTINUE)

    def input_password(self):
        self.input_text(self.PASSWORD, 'Asdfghjkl')
        self.click(self.LOGIN)








