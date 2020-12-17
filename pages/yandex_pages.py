from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import YandexSearchLocators, YandexPictureLocators
import time
from selenium.webdriver.common.by import By


class TaskPage(BasePage):
    def search_in_yandex(self, word):
        assert self.is_element_present(*YandexSearchLocators.YANDEX_SEARCH_FIELD), "Поле поиска отсутсвует"
        search_field = self.browser.find_element(*YandexSearchLocators.YANDEX_SEARCH_FIELD)
        search_field.send_keys(word)

    def checking_suggest(self):
        assert self.is_element_present(*YandexSearchLocators.SUGGEST), 'Таблица с подсказками отсутствует'

    def click_on_the_search_button(self):
        assert self.is_element_present(*YandexSearchLocators.YANDEX_SEARCH_BUTTON), 'Кнопка найти отсутствует'
        search_button = self.browser.find_element(*YandexSearchLocators.YANDEX_SEARCH_BUTTON)
        search_button.click()
        # click_enter.send_keys(Keys.ENTER)

    def checking_the_results(self):
        first_five = self.browser.find_elements(*YandexSearchLocators.SEARCH_RESULTS)[:5]
        for result in first_five:
            assert 'tensor.ru' in result.text.lower()


    def go_to_page_images_yandex(self):
        assert self.is_element_present(*YandexPictureLocators.YANDEX_IMAGE_LINK), "Ссылка на картинки отсутствует"
        images_link = self.browser.find_element(*YandexPictureLocators.YANDEX_IMAGE_LINK)
        images_link.click()

    def switch_to_page(self):
        tabs = self.browser.window_handles  # список
        self.browser.switch_to.window(tabs[1])

    def click_images(self):
        images = self.browser.find_elements(*YandexPictureLocators.SELECTING_IMAGES_THEME)
        images_theme = images[0] # Выбор темы изображения
        images_theme.click()
