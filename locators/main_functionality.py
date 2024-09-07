from selenium.webdriver.common.by import By

CONSTRUCTOR = (By.XPATH, './/p[text()="Конструктор"]')
ORDER_FEED = (By.XPATH, './/p[text()="Лента Заказов"]')
INGREDIENT = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")
CLOSE_MODAL_WINDOW = (By.XPATH, '//button[contains(@class,"close")]')
SHOPPING_BAG = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
COUNTER = (By.XPATH, './/p[@class="counter_counter__num__3nue1"]')
CREATE_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
#text_order = (By.XPATH, './/p[@class="undefined text text_type_main-small mb-2"]')
LOGIN_IN_ACCOUNT = (By.XPATH, './/*[@id="root"]/div/main/section[2]/div/button')
PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')
order_successfully_created = (By.XPATH, "//p[text()='идентификатор заказа']")
MODAL_WINDOW = (By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/div/h2')
