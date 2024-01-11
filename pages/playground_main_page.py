from locators.main_page_locators import DYNAMIC_ID_PAGE
from pages.base_page import BasePage


class PlaygroundMainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to_main_page(self):
        self.navigate()

    def navigate_to_dynamic_id(self):
        self.click_on(DYNAMIC_ID_PAGE)
