from pages.yandex_pages import TaskPage


def test_search_in_yandex(browser):
    yandex_main_page = TaskPage(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.search_in_yandex('Тензор')


