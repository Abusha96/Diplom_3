from selenium.webdriver.common.by import By

profile_button = (By.XPATH, ".//a[text() = 'Профиль']")
order_history_button = (By.XPATH, ".//a[text() = 'История заказов']")
history_item_window = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")
logout_button = (By.XPATH, ".//button[text() = 'Выход']")
personal_account = (By.XPATH, '//*[@id="root"]/div/header/nav/a')
