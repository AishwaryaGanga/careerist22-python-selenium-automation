from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class TermsAndConditionsPage(Page):

    def verify_terms_and_conditions_page_opened(self):
        self.verify_partial_url("https://www.target.com/c/terms-conditions/")

    def close_new_open_old_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)


