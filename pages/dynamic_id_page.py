from playwright.sync_api import Page

from pages.base_page import BasePage


class DynamicId(BasePage):
    adding_url: str = "dynamicid"

    def __init__(self, page: Page):
        super().__init__(page)
