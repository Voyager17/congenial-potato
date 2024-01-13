from pages.base_page import BasePage


class AttributeClass(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page.on("dialog", self.getting_message_from_alert)
        self.dialog_message = ""

    def getting_message_from_alert(self, dialog):
        self.dialog_message = dialog.message
        dialog.accept()
