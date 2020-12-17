from selenium.webdriver.common.by import By


class YandexSearchLocators:
    YANDEX_SEARCH_FIELD = (By.ID, "text")
    SUGGEST = (By.CLASS_NAME, "mini-suggest__popup_visible")
    YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    SEARCH_RESULTS = (By.CLASS_NAME, "organic typo typo_text_m typo_line_s i-bem")
    YANDEX_IMAGE_LINK = (By.XPATH, "//a[@data-id='images']")
