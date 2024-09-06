from selenium.webdriver.common.by import By

login_email_input = (By.XPATH, ".//input[@name = 'name']")
login_password_input = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
login_button = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
login_show_password = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
login_recovery_password_input = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div')
login_forgot_password = (By.XPATH, "//a[text() = 'Восстановить пароль']")
login_password_reset = (By.XPATH, "//button[text() = 'Восстановить']")
