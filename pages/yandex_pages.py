from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import YandexSearchLocators
import time

class TaskPage(BasePage):
    def search_in_yandex(self, word):
        assert self.is_element_present(*YandexSearchLocators.YANDEX_SEARCH_FIELD), "Поле поиска отсутсвует"
        search_field = self.browser.find_element(*YandexSearchLocators.YANDEX_SEARCH_FIELD)
        search_field.send_keys(word)
        assert self.is_element_present(*YandexSearchLocators.SUGGEST), 'Таблица с подсказками отсутствует'
        time.sleep(5)
        search_field.send_keys(Keys.ENTER)
