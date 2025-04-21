from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC



class SignInPage(Page):
    #SIGN_IN_TEXT = (By.CSS_SELECTOR, ".styles_ndsHeading__HcGpD")
    EMAIL = (By.ID, '#username')
    CONTINUE = (By.ID, 'continue')
    PASSWORD = (By.ID, 'password')
    LOGIN = (By.ID, 'login')
    PRIVACY_POLICY = (By.CSS_SELECTOR,"[aria-label *= 'terms & conditions']" )
    SIGN_IN = (By.CSS_SELECTOR, ".sc-43f80224-3.fBDEOp.h-margin-r-x3")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "[data-test = 'accountNav-signIn']")


    def open_target_sign_in_page(self):
        self.open_url("https://mytargetcirclecard.target.com/ecs/auth/?cid=AAAA6331001")
        sleep(5)

    def store_original_window(self):
        self.current_window_handle = self.driver.current_window_handle
        print("Current window handle: ",self.current_window_handle)

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

    def click_login_page(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGN_IN)).click()
        self.wait.until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON)).click()










