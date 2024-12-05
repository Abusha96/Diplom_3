from selenium.webdriver.common.by import By

ORDER_1 = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]/a')
MODAL_WINDOW = (By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div')
TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
IN_PROGRESS_ORDER_COUNT = (By.XPATH, './/ul[contains(@class,"OrderFeed_orderListReady")]/li[@class="text text_type_digits-default mb-2"]')
ORDER_HISTORY_ITEM_ID = (By.XPATH, './/p[@class="text text_type_digits-default"]')
ORDER_ID = (By.XPATH, '//*[@id="root"]/div/section/div[1]/div/h2')
