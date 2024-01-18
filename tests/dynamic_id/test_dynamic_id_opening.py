from typing import Optional

import allure
from playwright.sync_api import Page

from locators.dynamic_id_page_locators import BUTTON_WITH_DYNAMIC_ID_BUTTON
from pages.dynamic_id_page import DynamicId
from pages.playground_main_page import PlaygroundMainPage


def test_opening_dynamic_id_page(page: Page) -> None:
    main_page = PlaygroundMainPage(page)
    main_page.navigate_to_main_page()
    main_page.navigate_to_dynamic_id_page()

    with allure.step("Getting id from Dynamic Id page"):
        dynamic_id_page = DynamicId(page)
        id: Optional[str] = dynamic_id_page.getting_id_of_element_by_locator(
            BUTTON_WITH_DYNAMIC_ID_BUTTON
        )
    assert id is not None, "Id is missed. Check Dynamic Page"
    print(f"Id = {id}")
