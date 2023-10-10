import allure

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class IndexPage(BasePage):
    TOP_NAVIGATION = (By.CSS_SELECTOR, '#top')
    LOGO = (By.CSS_SELECTOR, '#logo')
    SEARCH_STRING = (By.CSS_SELECTOR, '[name=search]')
    MENU = (By.CSS_SELECTOR, '#menu')
    CART_BUTTON = (By.CSS_SELECTOR, '#cart > button')
    CURRENCY_BUTTON = (By.XPATH, '//*[@id="form-currency"]/div/button')
    EURO = (By.CSS_SELECTOR, 'button[name=EUR]')
    EURO_LOGO = (By.XPATH, "//strong[contains(text(), '€')]")
    POUND = (By.CSS_SELECTOR, 'button[name=GBP]')
    POUND_LOGO = (By.XPATH, "//strong[contains(text(), '£')]")
    DOLLAR = (By.CSS_SELECTOR, 'button[name=USD]')
    DOLLAR_LOGO = (By.XPATH, "//strong[contains(text(), '$')]")

    @allure.step("Открытие списка валют")
    def click_currency_button(self):
        self.click(self.wait_element(self.CURRENCY_BUTTON))

    @allure.step("Выбор Евро")
    def choose_euro(self):
        self.click_currency_button()
        self.click(self.wait_element(self.EURO))
        assert self.wait_element(self.EURO_LOGO)

    @allure.step("Выбор Фунта")
    def choose_pound(self):
        self.click_currency_button()
        self.click(self.wait_element(self.POUND))
        assert self.wait_element(self.POUND_LOGO)

    @allure.step("Выбор Доллара")
    def choose_dollar(self):
        self.click_currency_button()
        self.click(self.wait_element(self.DOLLAR))
        assert self.wait_element(self.DOLLAR_LOGO)
