from playwright.sync_api import Page, Dialog

from pages.base_page import BasePage


class AttributeClass(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.on("dialog", self.getting_message_from_alert)
        self.dialog_message: str = ""

    def getting_message_from_alert(self, dialog: Dialog) -> None:
        self.dialog_message: str = dialog.message
        dialog.accept()
