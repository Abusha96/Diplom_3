import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function", params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        firefox_driver = webdriver.Firefox(options=options)
        firefox_driver.set_window_size(1920, 1080)
        yield firefox_driver
        firefox_driver.quit()
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        chrome_driver = webdriver.Chrome(options=options)
        yield chrome_driver
        chrome_driver.quit()


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 10)
    yield wait
