from pages.yandex_pages import TaskPage
import time


def test_search_in_yandex(browser):
    yandex_main_page = TaskPage(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.search_in_yandex('Тензор')
    yandex_main_page.checking_suggest()
    yandex_main_page.click_on_the_search_button()
    time.sleep(1)
    yandex_main_page.checking_the_results()


# def test_yandex_images(browser):
#     yandex_page = TaskPage(browser)
#     yandex_page.go_to_site()
#     yandex_page.go_to_page_images_yandex()
#     yandex_page.switch_to_page()
#     yandex_page.click_images()

