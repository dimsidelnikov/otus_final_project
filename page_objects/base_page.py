import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = driver.logger
        self.class_name = type(self).__name__

    @allure.step
    def wait_element(self, selector, timeout=1):
        self.logger.info("%s: Check if element %s is present" % (self.class_name, str(selector)))
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(selector))
        except TimeoutException:
            self.logger.error("%s: Element %s is not present" % (self.class_name, str(selector)))
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f"{self.driver.current_url}",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError("didn't wait for the visibility of the element: {}".format(selector))

    @allure.step
    def wait_elements(self, selector, timeout=1):
        self.logger.info("%s: Check if elements %s are present" % (self.class_name, str(selector)))
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(selector))
        except TimeoutException:
            self.logger.error("%s: Element %s are not present" % (self.class_name, str(selector)))
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f"{self.driver.current_url}",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError("didn't wait for the visibility of the elements: {}".format(selector))

    @allure.step
    def click(self, element):
        self.logger.info("%s: Clicking element: %s" % (self.class_name, element))
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    @allure.step
    def input(self, element, value):
        self.click(element)
        self.logger.info("%s: Input '%s' in input %s" % (self.class_name, value, element))
        element.clear()
        element.send_keys(value)
