from faker import Faker
from locators.locators_order import LocatorsOrder
from pages.base_page import BasePage
from constants import Constants
import allure



class ZakazOrderPage(BasePage):



    @allure.step('Заполнение первой страницы формы заказа')
    def fill_order_form(self):
        self.wait_for_visibility(LocatorsOrder.ORDER_FORM)
        self.send_data_to_locator(LocatorsOrder.NAME_FIELD, Constants.NAME_FIELD)
        self.send_data_to_locator(LocatorsOrder.SURNAME_FIELD, Constants.SURNAME_FIELD)
        self.send_data_to_locator(LocatorsOrder.ADDRESS_FIELD, Constants.ADDRESS_FIELD)
        self.click(LocatorsOrder.METRO_FIELD)
        self.wait_for_visibility(LocatorsOrder.METRO_LIST)
        self.click(LocatorsOrder.CHOOSE_METRO_FIELD)
        self.send_data_to_locator(LocatorsOrder.PHONE_FIELD, Constants.PHONE_FIELD)
        self.click(LocatorsOrder.BUTTON_NEXT)

    @allure.step('Заполнение второй страницы формы заказа')
    def fill_rent_form(self):

        faker = Faker()
        fake_date = faker.date_between(start_date='today', end_date='+1y')
        date = fake_date.strftime("%Y-%m-%d")

        self.send_data_to_locator(LocatorsOrder.DATE_FIELD, date)
        self.click(LocatorsOrder.BLACK_CHECKOX)
        self.click(LocatorsOrder.RENTAL_FIELD)
        self.wait_for_visibility(LocatorsOrder.RENTAL_LIST)
        self.click(LocatorsOrder.CHOOSE_MENU_FIELD)
        self.send_data_to_locator(LocatorsOrder.COMMENT_FIELD, Constants.СOMMENT)
        self.click(LocatorsOrder.ORDER_BUTTON)
        self.wait_for_visibility(LocatorsOrder.AGREE_BUTTON)
        self.click(LocatorsOrder.AGREE_BUTTON)
        self.wait_for_visibility(LocatorsOrder.SUCCESS_ORDER)

    @allure.step('Заполнение первой страницы формы заказа доп данными')
    def fill_order_form_alt(self):

        faker = Faker()
        fake_date = faker.date_between(start_date='today', end_date='+1y')
        date = fake_date.strftime("%Y-%m-%d")


        self.wait_for_visibility(LocatorsOrder.ORDER_FORM)
        self.send_data_to_locator(LocatorsOrder.NAME_FIELD, Constants.NAME_FIELD_ALT)
        self.send_data_to_locator(LocatorsOrder.SURNAME_FIELD, Constants.SURNAME_FIELD_ALT)
        self.send_data_to_locator(LocatorsOrder.ADDRESS_FIELD, Constants.ADDRESS_FIELD_ALT)
        self.click(LocatorsOrder.METRO_FIELD)
        self.wait_for_visibility(LocatorsOrder.METRO_LIST)
        self.click(LocatorsOrder.CHOOSE_METRO_FIELD_ADD)
        self.send_data_to_locator(LocatorsOrder.PHONE_FIELD, Constants.PHONE_FIELD_ALT)
        self.click(LocatorsOrder.BUTTON_NEXT)

    @allure.step('Заполнение второй страницы формы заказа доп данными')
    def fill_rent_form_alt(self):


        faker = Faker()
        fake_date = faker.date_between(start_date='today', end_date='+1y')
        date = fake_date.strftime("%Y-%m-%d")

        self.send_data_to_locator(LocatorsOrder.DATE_FIELD, date)
        self.click(LocatorsOrder.GREY_CHECBOX)
        self.click(LocatorsOrder.RENTAL_FIELD)
        self.wait_for_visibility(LocatorsOrder.RENTAL_LIST)
        self.click(LocatorsOrder.CHOOSE_MENU_FIELD_ADD)
        self.send_data_to_locator(LocatorsOrder.COMMENT_FIELD, Constants.COMMENT_ALT)
        self.click(LocatorsOrder.ORDER_BUTTON)
        self.wait_for_visibility(LocatorsOrder.AGREE_BUTTON)
        self.click(LocatorsOrder.AGREE_BUTTON)
        self.wait_for_visibility(LocatorsOrder.SUCCESS_ORDER)

    @allure.step('Получение окна подтверждения заказа')
    def get_confirmation_window_header(self):
        return self.text_extracting(LocatorsOrder.CONFIRMATION_HEADER)

