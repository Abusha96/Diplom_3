from selenium.webdriver.common.by import By

#orders = (By.XPATH, './/h2[@class="text text_type_main-medium mb-2"][1]')
#details = (By.XPATH, '//p[text()="Cостав"]')
#title = (By.XPATH, '//h1[text()="Лента заказов"]')
total_order_count = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
daily_order_count = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
in_progress_order_count = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")
order_window = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")
order_history = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')
order_id = (By.XPATH, './/p[@class="text text_type_digits-default"]')
order_history_item_id = (By.XPATH, './/p[@class="text text_type_digits-default"]')
