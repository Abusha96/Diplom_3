import allure

from locators.order_feed_section import ORDER_FEED, MODAL_WINDOW, ORDER_1, ORDER_HISTORY_ITEM_ID, TOTAL_ORDER_COUNT, \
    DAILY_ORDER_COUNT, IN_PROGRESS_ORDER_COUNT
from pages.base_page import BasePage
from urls import URLS


class OrderFeedPage(BasePage):

    @allure.step("Клик по заказу")
    def click_to_order(self):
        self.check_element_visibility(ORDER_1)
        self.force_click(ORDER_1)

    @allure.step("Проверить, что модальное окно открыто")
    def check_modal_window_is_opened(self):
        return self.find_element(MODAL_WINDOW)

    @allure.step("Получить id последнего заказа")
    def get_the_last_order_id(self):
        return [el.text for el in self.find_elements(ORDER_HISTORY_ITEM_ID)]

    @allure.step("Перейти на страницу заказов")
    def open_url_feed(self):
        self.driver.get(URLS.URL_FEED)

    @allure.step("Получить общее количество заказов")
    def get_total_count(self):
        return self.find_text_element(TOTAL_ORDER_COUNT)

    @allure.step("Получить количество сегодняшних заказов")
    def get_daily_count(self):
        return self.find_text_element(DAILY_ORDER_COUNT)

    @allure.step("Получить заказы «В работе»")
    def get_in_progress_orders(self):
        return [el.text for el in self.find_elements(IN_PROGRESS_ORDER_COUNT)]
