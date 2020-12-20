from pages.yandex_search_pages import SearchPage
from pages.yandex_images_page import ImagesPage
import allure


@allure.title("Поиск в яндексе")
def test_search_in_yandex(browser):
    yandex_main_page = SearchPage(browser)
    yandex_main_page.go_to_site()
    with allure.step("Проверка наличия поиска"):
        yandex_main_page.search_in_yandex('Тензор')
    with allure.step("Проверка на то, что появилась таблица с подсказками (suggest)"):
        yandex_main_page.checking_suggest()
    with allure.step("При нажатии Enter появляется таблица результатов поиска"):
        yandex_main_page.click_on_the_search()
        yandex_main_page.checking_table_results()
    with allure.step("В первых 5 результатах есть ссылка на tensor.ru"):
        yandex_main_page.checking_search_results()


@allure.title("Картинки на яндексе")
def test_yandex_images(browser):
    yandex_page = ImagesPage(browser)
    yandex_page.go_to_site()
    with allure.step("Ссылка «Картинки» присутствует на странице"):
        yandex_page.go_to_page_images_yandex()
    yandex_page.switch_to_page()
    with allure.step("Проверка на то, что перешли на url https://yandex.ru/images/"):
        yandex_page.checking_current_url()
    with allure.step("Открыть категорию, проверить что открылась, в поиске верный текст"):
        yandex_page.click_theme_images()
    with allure.step("Открыть 1 картинку, проверить что открылась"):
        yandex_page.click_images()
    with allure.step("При нажатии кнопки вперед картинка изменяется,"
                     "При нажатии кнопки назад картинка изменяется на то же изображение"):
        yandex_page.check_images()


