from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class YandexSearchLocators:
    YANDEX_SEARCH_FIELD = (By.ID, "text")
    SUGGEST = (By.CLASS_NAME, "mini-suggest__popup_visible")
    RESULTS_TABLE = (By.CSS_SELECTOR, '[class="organic__title-wrapper typo typo_text_l typo_line_m"]')
    SEARCH_RESULTS = (By.CLASS_NAME, "path.organic__path")


class SearchPage(BasePage):

    def search_in_yandex(self, word):
        """
        Ввод в поле поиска текста запроса
        :param word: текст запроса
        """
        assert self.is_element_present(*YandexSearchLocators.YANDEX_SEARCH_FIELD), "Поле поиска отсутсвует"
        search_field = self.browser.find_element(*YandexSearchLocators.YANDEX_SEARCH_FIELD)
        search_field.send_keys(word)

    def checking_suggest(self):
        """Проверка таблицы с подсказками"""
        assert self.is_element_present(*YandexSearchLocators.SUGGEST), 'Таблица с подсказками отсутствует'

    def click_on_the_search(self):
        """Нажатие кнопки enter"""
        sleep(1)
        pressing_enter = self.browser.find_element(*YandexSearchLocators.YANDEX_SEARCH_FIELD)
        pressing_enter.send_keys(Keys.ENTER)

    def checking_table_results(self):
        """Проверка таблицы результата поиска"""
        assert self.is_element_present(*YandexSearchLocators.RESULTS_TABLE), "Резултатов не найдено"

    def checking_search_results(self):
        """Проверка результатов поиска"""
        first_five = self.browser.find_elements(*YandexSearchLocators.SEARCH_RESULTS)[:5]
        for result in first_five:
            assert 'tensor.ru' in result.text, "В первых пяти результатах нет ссылки"



