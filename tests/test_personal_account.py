import allure

from pages.personal_account_page import PersonalAccountPage
from urls import URLS


class TestPersonalAccount:

    @allure.title('Переход по клику на «Личный кабинет»')
    def test_redirect_to_personal_account(self, driver): # РАБОТАЕТ!
        redirect_to_personal_account = PersonalAccountPage(driver, self.wait)
        redirect_to_personal_account.open_personal_account_page()
        assert redirect_to_personal_account.get_url() == URLS.URL_LOGIN

    @allure.title('Переход в раздел «История заказов»')
    def test_redirect_to_order_history_section(self, driver): # Работает!!!!
        redirect_to_order_history_section = PersonalAccountPage(driver, self.wait)
        redirect_to_order_history_section.login()
        redirect_to_order_history_section.click_on_personal_account_button()
        redirect_to_order_history_section.click_on_order_history()
        assert redirect_to_order_history_section.get_url() == URLS.URL_ORDER_HISTORY

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver): # Работает !!!!!
        logout = PersonalAccountPage(driver, self.wait)
        logout.login()
        logout.click_on_personal_account_button()
        logout.click_on_logout_button()
        logout.get_url()
        logout.url_to_be(URLS.URL_LOGIN)
        assert logout.get_url() == URLS.URL_LOGIN
