from locators.main_functionality import constructor, order_feed, ingredient, close_modal_window, counter, \
    basket, modal_window, create_order_button
from locators.order_feed_section import order_id
from pages.base_page import BasePage
from urls import URLS


class MainFunctionalityPage(BasePage):

    def open_main_page(self):
        self.open_url(URLS.BASE_URL)

    def click_to_constructor(self):
        self.click_element(constructor)

    def click_to_order_feed(self):
        self.click_element(order_feed)

    def click_to_ingredient(self):
        self.click_element(ingredient)

    def check_modal_window(self):
        self.wait.until(lambda x: not self.driver.find_element(*modal_window))
        return self.driver.find_element(*modal_window)

    def close_modal_window(self):
        self.click_element(close_modal_window)
        self.check_element_clickable(constructor)

    def add_ingredient_to_order(self):
        self.drag_drop(ingredient, basket)

    def check_count_of_ingredient(self):
        return self.check_text(counter)

    def create_order(self):
        self.click_element(create_order_button)

    def check_order_successfully_created(self):
        return self.find_element(order_id)
