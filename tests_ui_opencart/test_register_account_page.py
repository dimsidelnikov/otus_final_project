import allure

from page_objects.register_account_page import RegisterAccountPage
from urllib.parse import urljoin

reg_page_path = 'index.php?route=account/register'
success_reg_path = 'index.php?route=account/success'
success_title = 'Your Account Has Been Created!'


@allure.title("Тест обнаружения элементов")
def test_register_account_page_find_elements(browser):
    browser.get(urljoin(browser.url, reg_page_path))
    RegisterAccountPage(browser).wait_element(RegisterAccountPage.FIRSTNAME_INPUT)
    RegisterAccountPage(browser).wait_element(RegisterAccountPage.LASTNAME_INPUT)
    RegisterAccountPage(browser).wait_element(RegisterAccountPage.EMAIL_INPUT)
    RegisterAccountPage(browser).wait_element(RegisterAccountPage.TELEPHONE_INPUT)
    RegisterAccountPage(browser).wait_element(RegisterAccountPage.PASSWORD_INPUT)
    RegisterAccountPage(browser).wait_element(RegisterAccountPage.CONFIRM_INPUT)
    RegisterAccountPage(browser).wait_element(RegisterAccountPage.PRIVACY_POLICY)

    submit_button = RegisterAccountPage(browser).wait_element(RegisterAccountPage.SUBMIT_BUTTON)

    RegisterAccountPage(browser).click(submit_button)
    RegisterAccountPage(browser).wait_element(RegisterAccountPage.WARNING_PRIVACY_POLICY, 0.5)


@allure.title("Тест регистрации нового пользователя")
def test_reg_new_user(browser):
    browser.get(urljoin(browser.url, reg_page_path))
    RegisterAccountPage(browser).input_new_user_info()
    RegisterAccountPage(browser).agree_with_privacy_policy()
    RegisterAccountPage(browser).create_user(urljoin(browser.url, success_reg_path), success_title)
