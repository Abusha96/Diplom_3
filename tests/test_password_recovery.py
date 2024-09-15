import allure

from pages.password_recovery_page import PasswordRecoveryPage
from urls import URLS


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_redirect_to_recovery_password_page(self, driver): # Работает!
        recovery_password_page = PasswordRecoveryPage(driver, self.wait)
        recovery_password_page.open_recovery_password_page()
        assert recovery_password_page.get_url() == URLS.URL_FORGOT_PASSWORD

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_and_button_is_clickable(self, driver): # Работает!
        recovery_password_page = PasswordRecoveryPage(driver, self.wait)
        recovery_password_page.open_recovery_password_page()
        recovery_password_page.input_email_and_click_recovery()
        recovery_password_page.wait_loading(recovery_password_page.get_url())
        assert recovery_password_page.get_url() == URLS.URL_RESET_PASSWORD

    @allure.title('Активация поля «Пароль» при клике на кнопку показать/скрыть пароль')
    def test_activate_field_after_click_on_eye(self, driver): # Работает!
        recovery_password_page = PasswordRecoveryPage(driver, self.wait)
        recovery_password_page.open_recovery_password_page()
        recovery_password_page.input_email_and_click_recovery()
        recovery_password_page.wait_loading(recovery_password_page.get_url())
        status_1 = recovery_password_page.return_type_of_input()
        recovery_password_page.click_on_show_password()
        status_2 = recovery_password_page.return_type_of_input()
        active_status = 'input_status_active'
        assert active_status not in status_1 and active_status in status_2
