from pages.base_page import BasePage


class DynamicId(BasePage):
    adding_url = "dynamicid"

    def __init__(self, page):
        super().__init__(page)
