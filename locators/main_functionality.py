from selenium.webdriver.common.by import By

constructor = (By.XPATH, './/p[text()="Конструктор"]')
order_feed = (By.XPATH, './/p[text()="Лента Заказов"]')
ingredient = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")
close_modal_window = (By.XPATH, '//button[contains(@class,"close")]')
basket = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
counter = (By.XPATH, './/p[@class="counter_counter__num__3nue1"]')
create_order_button = (By.XPATH, './/button[text()="Оформить заказ"]')
text_order = (By.XPATH, './/p[@class="undefined text text_type_main-small mb-2"]')
login_in_account = (By.XPATH, './/*[@id="root"]/div/main/section[2]/div/button')
order_id = (By.XPATH, "//p[text()='идентификатор заказа']")
modal_window = (By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/div/h2')
