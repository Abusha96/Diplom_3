from selenium import webdriver
from selenium.webdriver.common.by import By
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
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    def force_click(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def find_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element

    def find_elements(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        return elements

    def input(self, locator, keys):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(keys)

    def get_url(self):
        return self.driver.current_url

    def wait_loading(self, url):
        self.wait.until(lambda driver: url != self.get_url())

    def drag_drop(self, locator_1, locator_2):
        locator_1 = self.check_element_clickable(locator_1)
        locator_2 = self.check_element_clickable(locator_2)
        drag_and_drop(self.driver, locator_1, locator_2)

    def check_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def check_element_visibility(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def url_to_be(self, url, time=30):
        return WebDriverWait(self.driver, time).until(expected_conditions.url_to_be(url))

    def find_text_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).text

    def wait_until_secret_window_close(self, locator):
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, "//section[@class='Modal_modal__P3_V5']//div"
                                                                          "[@class='Modal_modal_overlay__x2ZCr']")))
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='Modal_modal__P3_V5']//div"
                                                                          "[@class='Modal_modal_overlay__x2ZCr']")))
        self.click_element(locator)
