from .base_page import BasePage
from selenium.webdriver.common.by import By


class YandexPictureLocators:
    YANDEX_IMAGE_LINK = (By.XPATH, "//a[@data-id='images']")
    SELECTING_IMAGES_THEME = (By.CLASS_NAME, "PopularRequestList-Shadow")
    SELECTING_IMAGES = (By.CLASS_NAME, "serp-item__link")
    NEXT_IMAGE_BUTTON = (By.CLASS_NAME, "CircleButton_type_next")
    PREVIOUS_IMAGE_BUTTON = (By.CLASS_NAME, "CircleButton_type_prev")


class ImagesPage(BasePage):

    def go_to_page_images_yandex(self):
        """Проверка ссылки и переход на сайт яндекс картинки"""
        assert self.is_element_present(*YandexPictureLocators.YANDEX_IMAGE_LINK), "Ссылка на картинки отсутствует"
        images_link = self.browser.find_element(*YandexPictureLocators.YANDEX_IMAGE_LINK)
        images_link.click()

    def checking_current_url(self):
        """Проверка перехода на url"""
        assert "https://yandex.ru/images/" in self.browser.current_url

    def switch_to_page(self):
        """Переключение на другое окно браузера"""
        tabs = self.browser.window_handles  # список отрывшихся вкладок
        self.browser.switch_to.window(tabs[1])

    def click_images(self):
        """Выбор темы изображений"""
        images = self.browser.find_elements(*YandexPictureLocators.SELECTING_IMAGES_THEME)
        images_theme = images[0] # Выбор темы изображения
        images_theme.click()