import allure

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class LoginAdminPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type=submit]')
    LOGO = (By.CSS_SELECTOR, 'img[title=OpenCart]')
    ALERT_DANGER = (By.CSS_SELECTOR, "div[class='alert alert-danger alert-dismissible']")

    @allure.step("Авторизация под пользователем {username}")
    def login(self, username, password):
        self.input(self.wait_element(self.USERNAME_INPUT), username)
        self.input(self.wait_element(self.PASSWORD_INPUT), password)
        self.click(self.wait_element(self.SUBMIT_BUTTON))
