import pytest
import logging
import datetime
import os

from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='http://10.0.2.15:8081/')
    parser.addoption('--maximize', action='store_true')
    parser.addoption('--headless', action='store_true')
    parser.addoption('--log_level', action='store', default='DEBUG')
    parser.addoption('--executor', default='127.0.0.1')
    parser.addoption("--bv")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('--browser')
    base_url = request.config.getoption('--url')
    maximize = request.config.getoption('--maximize')
    headless = request.config.getoption('--headless')
    log_level = request.config.getoption('--log_level')
    executor = request.config.getoption('--executor')
    version = request.config.getoption("--bv")

    executor_url = f"http://{executor}:4444/wd/hub"

    logs_dir = 'logs'
    os.makedirs(logs_dir, exist_ok=True)

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"{logs_dir}/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == 'chrome':
        options = ChromeOptions()
    elif browser_name == 'firefox':
        options = FirefoxOptions()
    elif browser_name == 'MicrosoftEdge':
        options = EdgeOptions()
    else:
        raise ValueError(f"Driver {browser_name} is not supported")

    options.set_capability("browserName", browser_name)
    options.set_capability("browserVersion", version)
    if headless:
        options.add_argument('--headless=new')
    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )

    if maximize:
        driver.maximize_window()

    driver.url = base_url
    driver.logger = logger

    logger.info("Browser %s started" % browser_name)

    yield driver

    driver.quit()
    logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))
