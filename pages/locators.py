from selenium.webdriver.common.by import By


class YandexSearchLocators:
    YANDEX_SEARCH_FIELD = (By.ID, "text")
    SUGGEST = (By.CLASS_NAME, "mini-suggest__popup_visible")
    YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    SEARCH_RESULTS = (By.CLASS_NAME, "organic typo typo_text_m typo_line_s i-bem")


class YandexPictureLocators:
    YANDEX_IMAGE_LINK = (By.XPATH, "//a[@data-id='images']")
    SELECTING_IMAGES_THEME = (By.CLASS_NAME, "PopularRequestList - Thumb")
    SELECTING_IMAGES = (By.CLASS_NAME, "serp-item__link")
    NEXT_IMAGE_BUTTON = (By.CLASS_NAME, "CircleButton_type_next")
    PREVIOUS_IMAGE_BUTTON = (By.CLASS_NAME, "CircleButton_type_prev")
