import allure

from page_objects.product_card_page import ProductCardPage
from urllib.parse import urljoin

macbook_path = 'laptop-notebook/macbook'


@allure.title("Тест обнаружения элементов")
def test_product_card_page_find_elements(browser):
    browser.get(urljoin(browser.url, macbook_path))
    ProductCardPage(browser).wait_element(ProductCardPage.PRODUCT_NAME)
    ProductCardPage(browser).wait_element(ProductCardPage.ADD_WISH_LIST_BUTTON)
    ProductCardPage(browser).wait_element(ProductCardPage.COST)
    ProductCardPage(browser).wait_element(ProductCardPage.QUANTITY_INPUT)
    ProductCardPage(browser).wait_element(ProductCardPage.ADD_CART_BUTTON)
