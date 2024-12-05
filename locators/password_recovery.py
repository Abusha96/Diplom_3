from selenium.webdriver.common.by import By

LOGIN_EMAIL_INPUT = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
LOGIN_PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
LOGIN_SHOW_PASSWORD = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
LOGIN_RECOVERY_PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div')
LOGIN_FORGOT_PASSWORD = (By.XPATH, "//a[text() = 'Восстановить пароль']")
LOGIN_PASSWORD_RESET = (By.XPATH, "//button[text() = 'Восстановить']")
