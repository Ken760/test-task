from .base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


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
        assert "https://yandex.ru/images/" in self.browser.current_url, 'Некорректный url'

    def switch_to_page(self):
        """Переключение на другое окно браузера"""
        tabs = self.browser.window_handles  # список отрывшихся вкладок
        self.browser.switch_to.window(tabs[1])

    def click_theme_images(self):
        """Выбор темы изображений"""
        images_theme = self.browser.find_elements(*YandexPictureLocators.SELECTING_IMAGES_THEME)
        selecting_images_theme = images_theme[0] # Выбор темы изображения
        selecting_images_theme.click()

    def click_images(self):
        """Выбор изображения из темы"""
        assert self.is_element_present(*YandexPictureLocators.SELECTING_IMAGES), "Изображение отсутствует"
        images = self.browser.find_elements(*YandexPictureLocators.SELECTING_IMAGES)
        selecting_images = images[0] # Выбор изображения
        selecting_images.click()

    def button_next_images(self):
        """Кнопка выбора следущей картинки"""
        assert self.is_element_present(*YandexPictureLocators.NEXT_IMAGE_BUTTON), \
            "Кнопка следущего изображения отсутствует"
        next_button = self.browser.find_element(*YandexPictureLocators.NEXT_IMAGE_BUTTON)
        next_button.click()
        sleep(1)

    def button_previous_images(self):
        """Кнопка выбора предыдущей картинки"""
        assert self.is_element_present(*YandexPictureLocators.PREVIOUS_IMAGE_BUTTON), \
            "Кнопка предыдущего изображения отсутствует"
        prev_button = self.browser.find_element(*YandexPictureLocators.PREVIOUS_IMAGE_BUTTON)
        prev_button.click()
        sleep(1)