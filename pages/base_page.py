from typing import Optional

from playwright.sync_api import Page

from locators.base_page_locators import *


class BasePage:
    BASE_URL: str = "http://uitestingplayground.com/"
    adding_url: str = ""

    def __init__(self, page: Page):
        self.page: Page = page
        self.url: str = self.BASE_URL + self.adding_url

    def click_on(self, selector: str) -> None:
        self.page.locator(selector).click()

    def navigate(self) -> None:
        self.page.goto(self.url)

    def navigate_to_home_page(self) -> None:
        self.click_on(HOME_BUTTON)

    def navigate_to_resources_page(self) -> None:
        self.click_on(RESOURCES_BUTTON)

    def getting_id_of_element_by_locator(self, selector: str) -> Optional[str]:
        return self.page.locator(selector).get_attribute("id")
