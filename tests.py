from pages.yandex_search_pages import SearchPage
from pages.yandex_images_page import ImagesPage
import time


# def test_search_in_yandex(browser):
#     yandex_main_page = SearchPage(browser)
#     yandex_main_page.go_to_site()
#     yandex_main_page.search_in_yandex('Тензор')
#     yandex_main_page.checking_suggest()
#     yandex_main_page.click_on_the_search()
#     yandex_main_page.checking_table_results()
#     yandex_main_page.checking_search_results()


def test_yandex_images(browser):
    yandex_page = ImagesPage(browser)
    yandex_page.go_to_site()
    yandex_page.go_to_page_images_yandex()
    yandex_page.switch_to_page()
    yandex_page.checking_current_url()
    yandex_page.click_theme_images()
    yandex_page.click_images()
    yandex_page.button_next_images()
    yandex_page.button_previous_images()
    time.sleep(5)

