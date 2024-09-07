from locators.order_feed_section import LOGIN_BUTTON_ON_MAIN, ORDER_FEED, MODAL_WINDOW, ORDER_1, order_history_item_id
from locators.password_recovery import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON
from pages.base_page import BasePage
from urls import URLS
from user_test_data import UserTestData


class OrderFeedPage(BasePage):

    def click_to_order_feed(self):
        self.click_element(ORDER_FEED)

    def click_to_order(self):
        self.click_element(ORDER_1)

    def check_modal_window_is_opened(self):
        return self.find_element(MODAL_WINDOW)

    def get_the_last_order_id(self):
        return self.find_element(order_history_item_id)[-1].text
