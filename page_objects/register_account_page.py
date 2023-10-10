import allure

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from helpers import random_string, random_email, random_phone


class RegisterAccountPage(BasePage):
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_INPUT = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    CONFIRM_INPUT = (By.CSS_SELECTOR, '#input-confirm')
    PRIVACY_POLICY = (By.LINK_TEXT, 'Privacy Policy')
    CHECKBOX_AGREE_POLICY = (By.CSS_SELECTOR, 'input[type=checkbox][name=agree]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[type=submit][value=Continue]')
    WARNING_PRIVACY_POLICY = (By.CSS_SELECTOR, '.alert')

    @allure.step("Ввод данных нового пользователя")
    def input_new_user_info(self):
        self.input(self.wait_element(self.FIRSTNAME_INPUT), random_string())
        self.input(self.wait_element(self.LASTNAME_INPUT), random_string())
        self.input(self.wait_element(self.EMAIL_INPUT), random_email())
        self.input(self.wait_element(self.TELEPHONE_INPUT), random_phone())

        password = random_string(5)

        self.input(self.wait_element(self.PASSWORD_INPUT), password)
        self.input(self.wait_element(self.CONFIRM_INPUT), password)

    @allure.step("Согласие с политикой конфиденциальности")
    def agree_with_privacy_policy(self):
        self.click(self.wait_element(self.CHECKBOX_AGREE_POLICY))

    @allure.step("Создание пользователя")
    def create_user(self, url, title):
        self.click(self.wait_element(self.SUBMIT_BUTTON))
        assert self.driver.current_url == url
        assert self.driver.title == title
