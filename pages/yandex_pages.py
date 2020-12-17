from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import YandexSearchLocators
from .locators import YandexPictureLocators
import time


class TaskPage(BasePage):
    def search_in_yandex(self, word):
        assert self.is_element_present(*YandexSearchLocators.YANDEX_SEARCH_FIELD), "Поле поиска отсутсвует"
        search_field = self.browser.find_element(*YandexSearchLocators.YANDEX_SEARCH_FIELD)
        search_field.send_keys(word)
        assert self.is_element_present(*YandexSearchLocators.SUGGEST), 'Таблица с подсказками отсутствует'
        time.sleep(5)
        search_field.send_keys(Keys.ENTER)

    def go_to_page_images_yandex(self):
        assert self.is_element_present(*YandexPictureLocators.YANDEX_IMAGE_LINK), "Ссылка на картинки отсутствует"
        images_link = self.browser.find_element(*YandexPictureLocators.YANDEX_IMAGE_LINK)
        images_link.click()

    def switch_to_page(self):
        tabs = self.browser.window_handles  # список
        browser.switch_to.window(tabs[1])

    def click_images(self):
        pass
