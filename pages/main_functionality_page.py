import allure

from locators.main_functionality import CONSTRUCTOR, ORDER_FEED, INGREDIENT, CLOSE_MODAL_WINDOW, \
    SHOPPING_BAG, MODAL_WINDOW, CREATE_ORDER_BUTTON, PERSONAL_ACCOUNT, ORDER_SUCCESSFULLY_CREATED
from locators.order_feed_section import ORDER_ID
from pages.base_page import BasePage
from urls import URLS


class MainFunctionalityPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_url(URLS.BASE_URL)

    @allure.step("Клик по кнопке «Конструктор»")
    def click_to_constructor(self):
        self.force_click(CONSTRUCTOR)

    @allure.step("Клик по кнопке «Лента заказов»")
    def click_to_order_feed(self):
        self.force_click(ORDER_FEED)

    @allure.step("Клик по ингредиенту")
    def click_to_ingredient(self):
        self.force_click(INGREDIENT)

    @allure.step("Проверить модальное окно")
    def check_modal_window(self):
        return self.check_element_clickable(INGREDIENT)

    @allure.step("Проверить текст в модальном окне")
    def check_text_modal_window(self):
        return self.find_element(MODAL_WINDOW).text

    @allure.step("Закрыть модальное окно")
    def close_modal_window(self):
        self.force_click(CLOSE_MODAL_WINDOW)
        self.check_element_clickable(PERSONAL_ACCOUNT)

    @allure.step("Добавить ингредиент к заказу")
    def add_ingredient_to_order(self):
        self.drag_drop(INGREDIENT, SHOPPING_BAG)

    @allure.step("Создать заказ")
    def create_order(self):
        self.click_element(CREATE_ORDER_BUTTON)

    @allure.step("Проверить, что заказ успешно создан")
    def check_order_successfully_created(self):
        return self.find_element(ORDER_SUCCESSFULLY_CREATED)

    @allure.step("Получить id заказа")
    def get_order_id(self):
        text = self.find_element(ORDER_ID).text
        self.wait.until(lambda x: text != self.find_element(ORDER_ID).text)
        return f'0{self.find_element(ORDER_ID).text}'
