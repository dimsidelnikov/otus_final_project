import allure

from page_objects.login_admin_page import LoginAdminPage
from page_objects.admin_page import AdminPage
from urllib.parse import urljoin
from test_data import users

admin_path = 'admin'


@allure.title("Тест добавления нового продукта")
def test_add_new_product(browser):
    browser.get(urljoin(browser.url, admin_path))
    LoginAdminPage(browser).login(users.ADMIN_USERNAME, users.ADMIN_PASSWORD)
    AdminPage(browser).move_to_page_products()
    AdminPage(browser).move_to_new_product()
    AdminPage(browser).input_new_product_info()
    AdminPage(browser).save_new_product()


@allure.title("Тест удаления продукта")
def test_delete_product(browser):
    browser.get(urljoin(browser.url, admin_path))
    LoginAdminPage(browser).login(users.ADMIN_USERNAME, users.ADMIN_PASSWORD)
    AdminPage(browser).move_to_page_products()
    AdminPage(browser).selection_product()
    AdminPage(browser).delete_product()
