from locators.password_recovery import login_email_input, login_button, login_password_input
from locators.personal_account import personal_account, order_history_button, logout_button
from pages.base_page import BasePage
from urls import URLS
from user_test_data import UserTestData


class PersonalAccountPage(BasePage):

    def open_personal_account_page(self):
        self.open_url(URLS.BASE_URL)
        self.click_element(personal_account)

    def login(self):
        self.open_url(URLS.BASE_URL)
        self.click_element(personal_account)
        self.click_element(login_email_input)
        self.input(login_email_input, UserTestData.EMAIL)
        self.click_element(login_password_input)
        self.input(login_password_input, UserTestData.PASSWORD)
        self.click_element(login_button)

    def click_on_personal_account_button(self):
        self.find_element(personal_account).click()

    def click_on_order_history(self):
        self.click_element(order_history_button)

    def click_on_logout_button(self):
        self.click_element(logout_button)
