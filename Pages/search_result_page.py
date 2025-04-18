from Pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

    def verify_search_results(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT)

    def verify_results_url(self, expected_partial_url):
            self.verify_partial_url(expected_partial_url)
