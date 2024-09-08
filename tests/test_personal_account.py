
from pages.personal_account_page import PersonalAccountPage
from urls import URLS


class TestPersonalAccount:

    def test_redirect_to_personal_account(self, driver, wait): # РАБОТАЕТ!
        redirect_to_personal_account = PersonalAccountPage(driver, wait)
        redirect_to_personal_account.open_personal_account_page()
        assert redirect_to_personal_account.get_url() == URLS.URL_LOGIN

    def test_redirect_to_order_history_section(self, driver, wait): # ВАЛИТСЯ один браузер (Mozilla)
        redirect_to_order_history_section = PersonalAccountPage(driver, wait)
        redirect_to_order_history_section.login()
        redirect_to_order_history_section.click_on_personal_account_button()
        redirect_to_order_history_section.click_on_order_history()
        assert redirect_to_order_history_section.get_url() == URLS.URL_ORDER_HISTORY

    def test_logout(self, driver, wait): # ВАЛИТСЯ один браузер (Mozilla)
        logout = PersonalAccountPage(driver, wait)
        logout.login()
        logout.click_on_personal_account_button()
        logout.click_on_logout_button()
        logout.get_url()
        logout.url_to_be(URLS.URL_LOGIN)
        assert logout.get_url() == URLS.URL_LOGIN
