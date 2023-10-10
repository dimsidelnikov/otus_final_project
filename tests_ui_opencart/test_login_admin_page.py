import allure
import pytest

from page_objects.login_admin_page import LoginAdminPage
from page_objects.admin_page import AdminPage
from test_data import users
from urllib.parse import urljoin

admin_path = 'admin'


@allure.title("Тест обнаружения элементов")
def test_login_admin_page_find_elements(browser):
    browser.get(urljoin(browser.url, admin_path))
    LoginAdminPage(browser).wait_element(LoginAdminPage.USERNAME_INPUT)
    LoginAdminPage(browser).wait_element(LoginAdminPage.PASSWORD_INPUT)
    LoginAdminPage(browser).wait_element(LoginAdminPage.FORGOTTEN_PASSWORD)
    LoginAdminPage(browser).wait_element(LoginAdminPage.SUBMIT_BUTTON)
    LoginAdminPage(browser).wait_element(LoginAdminPage.LOGO)


@pytest.mark.parametrize('username, password, expected_element',
                         [(users.ADMIN_USERNAME, users.ADMIN_PASSWORD, AdminPage.PROFILE_FOTO),
                          ('admin', '12345678', LoginAdminPage.ALERT_DANGER),
                          ('user', '', LoginAdminPage.ALERT_DANGER)],
                         ids=['valid credentials', 'invalid credentials', 'empty password'])
def test_admin_authorization(request, browser, username, password, expected_element):
    allure.dynamic.title(f'Тест авторизации c [{request.node.callspec.id}]')
    browser.get(urljoin(browser.url, admin_path))
    LoginAdminPage(browser).login(username, password)
    LoginAdminPage(browser).wait_element(expected_element)
