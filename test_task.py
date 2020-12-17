from pages.test_task_page import TaskPage


link = 'https://yandex.ru/'


def test_search_in_yandex(browser):
    search = TaskPage(browser, link)
    search.open()
    search.search_in_yandex()