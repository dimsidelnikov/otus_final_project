from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    CATEGORY_HEADER = (By.CSS_SELECTOR, '#content > h2')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '#list-view')
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, '#grid-view')
    SORTING_SELECTION = (By.CSS_SELECTOR, '#input-sort')
    LIMIT_SELECTION = (By.CSS_SELECTOR, '#input-limit')
