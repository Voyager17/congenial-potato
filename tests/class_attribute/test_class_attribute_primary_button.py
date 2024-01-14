from playwright.sync_api import Page

from locators.class_attribute_locators import PRIMARY_BUTTON
from pages.class_attribute_page import AttributeClass
from pages.playground_main_page import PlaygroundMainPage


def test_opening_dynamic_id_page(page: Page) -> None:
    main_page = PlaygroundMainPage(page)
    main_page.navigate_to_main_page()
    main_page.navigate_to_class_attribute_page()

    attribute_class_page = AttributeClass(page)
    attribute_class_page.click_on(PRIMARY_BUTTON)

    assert (
            attribute_class_page.dialog_message != ""
    ), "Primary button wasn't activated or dialog did not appear. Check the button functionality."

    print(f"Message from the alert = {attribute_class_page.dialog_message}")
