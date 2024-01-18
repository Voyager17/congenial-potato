import allure
from playwright.sync_api import Page

from locators.class_attribute_locators import (
    PRIMARY_BUTTON,
    WARNING_BUTTON,
    SUCCESS_BUTTON,
)
from pages.class_attribute_page import AttributeClass
from pages.playground_main_page import PlaygroundMainPage


@allure.title("Test clicking on the wrong buttons on the class attribute page")
@allure.description(
    "Test to ensure that primary button works after clicking on the wrong buttons"
)
def test_opening_dynamic_id_page(page: Page) -> None:
    main_page = PlaygroundMainPage(page)
    main_page.navigate_to_main_page()
    main_page.navigate_to_class_attribute_page()

    attribute_class_page = AttributeClass(page)
    attribute_class_page.click_on(WARNING_BUTTON)
    attribute_class_page.click_on(SUCCESS_BUTTON)
    attribute_class_page.click_on(PRIMARY_BUTTON)

    assert (
            attribute_class_page.dialog_message != ""
    ), "Primary button wasn't activated or dialog did not appear. Check the button functionality."

    print(f"Message from the alert = {attribute_class_page.dialog_message}")
