from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import TestPageLocators


class TaskPage(BasePage):
    def search_in_yandex(self):
        assert self.is_element_present(*TestPageLocators.INPUT_FIELD), "Поле поиска отсутсвует"
        search_field = self.browser.find_element(*TestPageLocators.INPUT_FIELD)
        search_field.send_keys('Тензор')
        assert self.is_element_present(*TestPageLocators.SUGGEST), 'Таблица с подсказками отсутствует'
        search_field.send_keys(Keys.ENTER)