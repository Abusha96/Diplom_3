import allure

from locators.main_functionality import COUNTER
from pages.main_functionality_page import MainFunctionalityPage
from pages.personal_account_page import PersonalAccountPage
from urls import URLS


class TestMainFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    def test_redirect_to_constructor(self, driver): # РАБОТАЕТ!
        redirect_to_constructor = MainFunctionalityPage(driver, self.wait)
        redirect_to_constructor.open_main_page()
        redirect_to_constructor.click_to_order_feed()
        redirect_to_constructor.click_to_constructor()
        assert redirect_to_constructor.get_url() == URLS.BASE_URL

    @allure.title('Переход по клику на «Лента заказов»')
    def test_redirect_to_order_feed(self, driver): # РАБОТАЕТ!
        redirect_to_order_feed = MainFunctionalityPage(driver, self.wait)
        redirect_to_order_feed.open_main_page()
        redirect_to_order_feed.click_to_order_feed()
        assert redirect_to_order_feed.get_url() == URLS.URL_FEED

    @allure.title('Появление всплывающего окна с деталями при клике на ингредиент')
    def test_modal_window_about_ingredient(self, driver): # РАБОТАЕТ!
        modal_window = MainFunctionalityPage(driver, self.wait)
        modal_window.open_main_page()
        modal_window.click_to_ingredient()
        assert "Детали ингредиента" in modal_window.check_text_modal_window()

    @allure.title('Закрытие всплывающего окна кликом на крестик')
    def test_close_modal_window_about_ingredient(self, driver): # РАБОТАЕТ!
        close_modal_window = MainFunctionalityPage(driver, self.wait)
        close_modal_window.open_main_page()
        close_modal_window.click_to_ingredient()
        close_modal_window.close_modal_window()
        assert close_modal_window.check_modal_window()

    @allure.title('Увеличение каунтера при добавлении ингредиента')
    def test_counter_increase_after_add_ingredient(self, driver): # РАБОТАЕТ!
        counter_check = MainFunctionalityPage(driver, self.wait)
        counter_check.open_main_page()
        counter_check.add_ingredient_to_order()
        assert '2' in counter_check.find_element(COUNTER).text

    @allure.title('Оформление заказа авторизованным пользователем')
    def test_authorized_user_create_order(self, driver): # РАБОТАЕТ!
        personal_account = PersonalAccountPage(driver, self.wait)
        create_order = MainFunctionalityPage(driver, self.wait)
        personal_account.login()
        create_order.create_order()
        assert "идентификатор заказа" in create_order.check_order_successfully_created().text
