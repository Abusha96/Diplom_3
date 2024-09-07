from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:

    def __init__(self, driver: webdriver.Firefox, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator)).click()

    def find_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element

    def input(self, locator, keys):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(keys)

    def get_url(self):
        return self.driver.current_url

    def wait_loading(self, url):
        self.wait.until(lambda driver: url != self.get_url())

    def check_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def scroll_to_element(self, locator):
        Q = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", Q)

    def open_new_page(self, text):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(lambda driver: text in driver.current_url)

    def drag_drop(self, locator_1, locator_2):
        locator_1 = self.check_element_clickable(locator_1)
        locator_2 = self.check_element_clickable(locator_2)
        drag_and_drop(self.driver, locator_1, locator_2)

    def check_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
