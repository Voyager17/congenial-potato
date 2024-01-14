from playwright.sync_api import Page

from locators.main_page_locators import (
    DYNAMIC_ID_PAGE,
    ATTRIBUTE_CLASS_PAGE,
)
from pages.base_page import BasePage


class PlaygroundMainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def navigate_to_main_page(self) -> None:
        self.navigate()

    def navigate_to_dynamic_id_page(self) -> None:
        self.click_on(DYNAMIC_ID_PAGE)

    def navigate_to_class_attribute_page(self) -> None:
        self.click_on(ATTRIBUTE_CLASS_PAGE)
