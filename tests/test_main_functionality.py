from locators.main_functionality import COUNTER, CREATE_ORDER_BUTTON
from pages.main_functionality_page import MainFunctionalityPage
from pages.personal_account_page import PersonalAccountPage
from urls import URLS


class TestMainFunctionality:

    def test_redirect_to_constructor(self, driver, wait): # РАБОТАЕТ!
        redirect_to_constructor = MainFunctionalityPage(driver, wait)
        redirect_to_constructor.open_main_page()
        redirect_to_constructor.click_to_order_feed()
        redirect_to_constructor.click_to_constructor()
        assert redirect_to_constructor.get_url() == URLS.BASE_URL

    def test_redirect_to_order_feed(self, driver, wait): # РАБОТАЕТ!
        redirect_to_order_feed = MainFunctionalityPage(driver, wait)
        redirect_to_order_feed.open_main_page()
        redirect_to_order_feed.click_to_order_feed()
        assert redirect_to_order_feed.get_url() == URLS.URL_FEED

    def test_modal_window_about_ingredient(self, driver, wait): # ПАДАЕТ :(
        modal_window = MainFunctionalityPage(driver, wait)
        modal_window.open_main_page()
        modal_window.click_to_ingredient()
        assert "Детали ингредиента" in modal_window.check_modal_window().text

    def test_close_modal_window_about_ingredient(self, driver, wait): # ПАДАЕТ :(
        close_modal_window = MainFunctionalityPage(driver, wait)
        close_modal_window.open_main_page()
        close_modal_window.click_to_ingredient()
        close_modal_window.close_modal_window()
        assert not close_modal_window.check_modal_window()

    def test_counter_increase_after_add_ingredient(self, driver, wait): # РАБОТАЕТ!
        counter_check = MainFunctionalityPage(driver, wait)
        counter_check.open_main_page()
        counter_check.add_ingredient_to_order()
        assert '2' in counter_check.find_element(COUNTER).text

    def test_authorized_user_create_order(self, driver, wait): # ПАДАЕТ :(
        personal_account = PersonalAccountPage(driver, wait)
        create_order = MainFunctionalityPage(driver, wait)
        personal_account.login()
        personal_account.wait_loading(personal_account.get_url())
        create_order.click_element(CREATE_ORDER_BUTTON)
        assert "идентификатор заказа" in create_order.check_order_successfully_created().text
