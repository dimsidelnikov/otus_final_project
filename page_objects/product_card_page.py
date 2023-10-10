from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductCardPage(BasePage):
    PRODUCT_NAME = (By.XPATH, '//*[@id="content"]/div/div[2]/h1')
    ADD_WISH_LIST_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Add to Wish List"]')
    COST = (By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[1]/h2')
    QUANTITY_INPUT = (By.CSS_SELECTOR, 'input[name=quantity]')
    ADD_CART_BUTTON = (By.CSS_SELECTOR, '#button-cart')
