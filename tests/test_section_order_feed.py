from pages.main_functionality_page import MainFunctionalityPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestSectionOrderFeed:

    def test_open_modal_window_after_click_on_order(self, driver, wait): # ПАДАЕТ один браузер
        personal_account = PersonalAccountPage(driver, wait)
        open_modal_window = OrderFeedPage(driver, wait)
        personal_account.login()
        open_modal_window.click_to_order_feed()
        open_modal_window.click_to_order()
        assert open_modal_window.check_modal_window_is_opened()

    def test_orders_display_in_order_feed(self, driver, wait): # ПАДАЕТ
        display_order = OrderFeedPage(driver, wait)
        personal_account = PersonalAccountPage(driver, wait)
        main_func = MainFunctionalityPage(driver, wait)
        personal_account.login()
        main_func.add_ingredient_to_order()
        main_func.create_order()
        order_num_1 = main_func.get_order_id()
        main_func.close_modal_window()
        personal_account.open_personal_account_page()
        personal_account.click_on_order_history()
        order_num_2 = display_order.get_the_last_order_id()
        assert order_num_1 == order_num_2

    def test_total_order_count_increases_after_new_order(self, driver, wait):
        pass

    def test_daily_order_count_increases_after_new_order(self, driver, wait):
        pass

    def test_order_id_display_in_progress_section(self, driver, wait):
        pass
