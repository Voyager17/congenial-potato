import time

from locators.main_page_locators import DYNAMIC_ID_PAGE
from pages.playground_main_page import PlaygroundMainPage


def test_opening_dynamic_id_page(page):
    main_page = PlaygroundMainPage(page)
    main_page.navigate()
    main_page.open(DYNAMIC_ID_PAGE)
    time.sleep(10)
