from locators.password_recovery import LOGIN_EMAIL_INPUT, LOGIN_BUTTON, LOGIN_PASSWORD_INPUT
from locators.personal_account import PERSONAL_ACCOUNT, ORDER_HISTORY_BUTTON, LOGOUT_BUTTON
from pages.base_page import BasePage
from urls import URLS
from user_test_data import UserTestData


class PersonalAccountPage(BasePage):

    def open_personal_account_page(self):
        self.open_url(URLS.BASE_URL)
        self.click_element(PERSONAL_ACCOUNT)

    def login(self):
        self.open_url(URLS.BASE_URL)
        self.click_element(PERSONAL_ACCOUNT)
        self.click_element(LOGIN_EMAIL_INPUT)
        self.input(LOGIN_EMAIL_INPUT, UserTestData.EMAIL)
        self.click_element(LOGIN_PASSWORD_INPUT)
        self.input(LOGIN_PASSWORD_INPUT, UserTestData.PASSWORD)
        self.click_element(LOGIN_BUTTON)

    def click_on_personal_account_button(self):
        self.find_element(PERSONAL_ACCOUNT).click()

    def click_on_order_history(self):
        self.click_element(ORDER_HISTORY_BUTTON)

    def click_on_logout_button(self):
        self.click_element(LOGOUT_BUTTON)
