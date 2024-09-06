from locators.main_functionality import login_in_account
from locators.password_recovery import login_forgot_password, login_email_input, login_password_reset, \
    login_show_password, login_recovery_password_input
from urls import URLS
from pages.base_page import BasePage
from user_test_data import UserTestData


class PasswordRecoveryPage(BasePage):

    def open_recovery_password_page(self):
        self.open_url(URLS.BASE_URL)
        self.click_element(login_in_account)
        self.click_element(login_forgot_password)

    def input_email_and_click_recovery(self):
        self.click_element(login_email_input)
        self.input(login_email_input, UserTestData.EMAIL)
        self.click_element(login_password_reset)

    def click_on_show_password(self):
        self.click_element(login_show_password)

    def return_type_of_input(self):
        type_element = self.find_element(locator=login_recovery_password_input).get_attribute('class')
        return type_element
