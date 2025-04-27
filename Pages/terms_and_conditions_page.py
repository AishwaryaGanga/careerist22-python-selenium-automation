from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class TermsAndConditionsPage(Page):

    def verify_terms_and_conditions_page_opened(self):
        self.verify_partial_url("https://www.target.com/c/terms-conditions/")



