import allure

from pages.main_functionality_page import MainFunctionalityPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestSectionOrderFeed:

    @allure.title('Открытие всплывающего окна с деталями при клике на заказ')
    def test_open_modal_window_after_click_on_order(self, driver, wait): # Работает!
        personal_account = PersonalAccountPage(driver, wait)
        open_modal_window = OrderFeedPage(driver, wait)
        personal_account.login()
        open_modal_window.open_url_feed()
        open_modal_window.click_to_order()
        assert open_modal_window.check_modal_window_is_opened()

    @allure.title('Отображение заказов пользователя из раздела «История заказов» на странице «Лента заказов»')
    def test_orders_display_in_order_feed(self, driver, wait): # Работает!
        display_order = OrderFeedPage(driver, wait)
        personal_account = PersonalAccountPage(driver, wait)
        main_func = MainFunctionalityPage(driver, wait)
        personal_account.login()
        main_func.add_ingredient_to_order()
        main_func.create_order()
        order_num_1 = main_func.get_order_id()
        main_func.close_modal_window()
        personal_account.click_on_personal_account_button()
        personal_account.click_on_order_history()
        display_order.open_url_feed()
        order_num_2 = display_order.get_the_last_order_id()
        assert '#' + order_num_1 in order_num_2

    @allure.title('Увеличение счетчика «Выполнено за всё время» при создании нового заказа')
    def test_total_order_count_increases_after_new_order(self, driver, wait): # Работает!
        display_order = OrderFeedPage(driver, wait)
        personal_account = PersonalAccountPage(driver, wait)
        main_func = MainFunctionalityPage(driver, wait)
        personal_account.login()
        personal_account.wait_loading(personal_account.get_url())
        display_order.open_url_feed()
        before = display_order.get_total_count()
        main_func.open_main_page()
        main_func.add_ingredient_to_order()
        main_func.create_order()
        display_order.open_url_feed()
        assert int(display_order.get_total_count()) > int(before)

    @allure.title('Увеличение счетчика «Выполнено за сегодня» при создании нового заказа')
    def test_daily_order_count_increases_after_new_order(self, driver, wait): # Работает!
        display_order = OrderFeedPage(driver, wait)
        personal_account = PersonalAccountPage(driver, wait)
        main_func = MainFunctionalityPage(driver, wait)
        personal_account.login()
        personal_account.wait_loading(personal_account.get_url())
        display_order.open_url_feed()
        before = display_order.get_daily_count()
        main_func.open_main_page()
        main_func.add_ingredient_to_order()
        main_func.create_order()
        display_order.open_url_feed()
        assert int(display_order.get_daily_count()) > int(before)

    @allure.title('Появление номера заказа в разделе «В работе»')
    def test_order_id_display_in_progress_section(self, driver, wait): # Что-то несусветное здесь происходит:
        # зачастую фактический номер заказа меньше на 1, чем ожидаемый результат. Запускала много раз, то успешно, то
        # валится
        display_order = OrderFeedPage(driver, wait)
        personal_account = PersonalAccountPage(driver, wait)
        main_func = MainFunctionalityPage(driver, wait)
        personal_account.login()
        main_func.add_ingredient_to_order()
        main_func.create_order()
        order_num_1 = main_func.get_order_id()
        main_func.close_modal_window()
        display_order.open_url_feed()
        assert order_num_1 in display_order.get_in_progress_orders()
