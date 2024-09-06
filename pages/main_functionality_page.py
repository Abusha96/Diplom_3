from locators.main_functionality import CONSTRUCTOR, ORDER_FEED, INGREDIENT, CLOSE_MODAL_WINDOW, COUNTER, \
    SHOPPING_BAG, MODAL_WINDOW, CREATE_ORDER_BUTTON
from locators.order_feed_section import order_id
from pages.base_page import BasePage
from urls import URLS


class MainFunctionalityPage(BasePage):

    def open_main_page(self):
        self.open_url(URLS.BASE_URL)

    def click_to_constructor(self):
        self.click_element(CONSTRUCTOR)

    def click_to_order_feed(self):
        self.click_element(ORDER_FEED)

    def click_to_ingredient(self):
        self.click_element(INGREDIENT)

    def check_modal_window(self):
        self.wait.until(lambda x: not self.driver.find_element(*MODAL_WINDOW))
        return self.driver.find_element(*MODAL_WINDOW)

    def close_modal_window(self):
        self.click_element(CLOSE_MODAL_WINDOW)
        self.check_element_clickable(CONSTRUCTOR)

    def add_ingredient_to_order(self):
        self.drag_drop(INGREDIENT, SHOPPING_BAG)

    def check_count_of_ingredient(self):
        return self.check_text(COUNTER)

    def create_order(self):
        self.click_element(CREATE_ORDER_BUTTON)

    def check_order_successfully_created(self):
        return self.find_element(order_id)
