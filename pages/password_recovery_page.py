from locators.main_functionality import LOGIN_IN_ACCOUNT
from locators.password_recovery import LOGIN_FORGOT_PASSWORD, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_RESET, \
    LOGIN_SHOW_PASSWORD, LOGIN_RECOVERY_PASSWORD_INPUT
from urls import URLS
from pages.base_page import BasePage
from user_test_data import UserTestData


class PasswordRecoveryPage(BasePage):

    def open_recovery_password_page(self):
        self.open_url(URLS.BASE_URL)
        self.click_element(LOGIN_IN_ACCOUNT)
        self.click_element(LOGIN_FORGOT_PASSWORD)

    def input_email_and_click_recovery(self):
        self.click_element(LOGIN_EMAIL_INPUT)
        self.input(LOGIN_EMAIL_INPUT, UserTestData.EMAIL)
        self.click_element(LOGIN_PASSWORD_RESET)

    def click_on_show_password(self):
        self.click_element(LOGIN_SHOW_PASSWORD)

    def return_type_of_input(self):
        type_element = self.find_element(locator=LOGIN_RECOVERY_PASSWORD_INPUT).get_attribute('class')
        return type_element
