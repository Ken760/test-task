from selenium.webdriver.common.by import By


class TestPageLocators:
    INPUT_FIELD = (By.ID, "text")
    SUGGEST = (By.CLASS_NAME, "mini-suggest__popup_visible")
    RESULTS = (By.CLASS_NAME, "organic typo typo_text_m typo_line_s i-bem")
    IMAGE_LINK = (By.XPATH, "//a[@data-id='images']")
