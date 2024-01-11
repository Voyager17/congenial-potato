from locators.base_page_locators import *


class BasePage:
    BASE_URL = "http://uitestingplayground.com/"
    adding_url = ""

    def __init__(self, page):
        self.page = page
        self.url = self.BASE_URL + self.adding_url

    def click_on(self, selector):
        self.page.locator(selector).click()

    def navigate(self):
        self.page.goto(self.url)

    def navigate_to_home_page(self):
        self.click_on(HOME_BUTTON)

    def navigate_to_resources_page(self):
        self.click_on(RESOURCES_BUTTON)

    def getting_id_of_element_by_locator(self, selector):
        return self.page.locator(selector).get_attribute("id")
