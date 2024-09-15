import allure

from locators.password_recovery import LOGIN_EMAIL_INPUT, LOGIN_BUTTON, LOGIN_PASSWORD_INPUT
from locators.personal_account import PERSONAL_ACCOUNT, ORDER_HISTORY_BUTTON, LOGOUT_BUTTON
from pages.base_page import BasePage
from urls import URLS
from user_test_data import UserTestData


class PersonalAccountPage(BasePage):

    @allure.step("Открыть личный кабинет")
    def open_personal_account_page(self):
        self.open_url(URLS.BASE_URL)
        self.force_click(PERSONAL_ACCOUNT)

    @allure.step("Залогиниться")
    def login(self):
        self.open_url(URLS.BASE_URL)
        self.force_click(PERSONAL_ACCOUNT)
        self.force_click(LOGIN_EMAIL_INPUT)
        self.input(LOGIN_EMAIL_INPUT, UserTestData.EMAIL)
        self.force_click(LOGIN_PASSWORD_INPUT)
        self.input(LOGIN_PASSWORD_INPUT, UserTestData.PASSWORD)
        self.force_click(LOGIN_BUTTON)

    @allure.step("Тап на кнопку «Личный кабинет»")
    def click_on_personal_account_button(self):
        self.click_element(PERSONAL_ACCOUNT)

    @allure.step("Тап на «История заказов»")
    def click_on_order_history(self):
        self.force_click(ORDER_HISTORY_BUTTON)

    @allure.step("Тап на «Выход»")
    def click_on_logout_button(self):
        self.click_element(LOGOUT_BUTTON)
