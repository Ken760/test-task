from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from selenium.webdriver.common.by import By
import time


class YandexSearchLocators:
    YANDEX_SEARCH_FIELD = (By.ID, "text")
    SUGGEST = (By.CLASS_NAME, "mini-suggest__popup_visible")
    SEARCH_RESULTS = (By.CLASS_NAME, "path.organic__path")


class SearchPage(BasePage):

    def search_in_yandex(self, word):
        """Ввод в поле поиска текста запроса"""
        assert self.is_element_present(*YandexSearchLocators.YANDEX_SEARCH_FIELD), "Поле поиска отсутсвует"
        search_field = self.browser.find_element(*YandexSearchLocators.YANDEX_SEARCH_FIELD)
        search_field.send_keys(word)

    def checking_suggest(self):
        """Проверка таблицы с подсказками"""
        assert self.is_element_present(*YandexSearchLocators.SUGGEST), 'Таблица с подсказками отсутствует'

    def click_on_the_search(self):
        """Нажатие кнопки enter"""
        pressing_enter = self.browser.find_element(*YandexSearchLocators.YANDEX_SEARCH_FIELD)
        pressing_enter.send_keys(Keys.ENTER)

    def checking_table_results(self):
        """Проверка таблицы результата поиска"""
        assert "По вашему запросу ничего не нашлось" not in self.browser.page_source, \
            "По вашему запросу ничего не нашлось"

    def checking_search_results(self):
        """Проверка результатов поиска"""
        first_five = self.browser.find_elements(*YandexSearchLocators.SEARCH_RESULTS)[:5]
        for result in first_five:
            assert 'tensor.ru' in result.text, "В первых пяти результатах нет ссылки"



