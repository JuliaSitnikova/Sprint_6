from locators.locators_faq import FaqLocators
from locators.locators_order import LocatorsOrder
from pages.base_page import BasePage
from locators.locators_logo import Logo
import allure


class ZakazMainPage(BasePage):

    @allure.step('Открытие браузера, вход на страницу аренды самоката')
    def open_zakaz_main_page(self):
        self.wait_for_visibility(FaqLocators.SCOOTER_IMAGE)

    @allure.step('Клик на логотип Яндекса')
    def ya_logo_click(self):
        self.click(Logo.YA_LOGO)

    @allure.step('Клик на логотип Самокат')
    def samokat_logo_click(self):
        self.click(Logo.LOGO_SAMOKAT)

    @allure.step('Клик на кнопку Заказать в шапке страницы')
    def order_button_click(self):
        self.click(Logo.ORDER_BUTTON)

    @allure.step('Клик на кнопку Статус заказа')
    def order_status_button_click(self):
        self.click(Logo.ORDER_STATUS_BUTTON)

    @allure.step('Клик на логотип Яндекса, переход на вкладку, ожидание загрузки логотипа')
    def logo_to_dzen(self):
        self.ya_logo_click()
        self.switch_to_window()
        self.wait_for_visibility(Logo.DZEN)

    @allure.step('Прокрутка скроллом вниз страницы')
    def scroll_to_bottom(self):
        self.scroll_to_element(FaqLocators.FAQ_7_Q)
        self.wait_for_visibility(FaqLocators.FAQ_7_Q)

    @allure.step('Прокрутка скроллом до кнопки Заказать на главной странице')
    def scroll_to_button(self):
        self.scroll_to_element(FaqLocators.ORDER_BUTTON_FIN)
        self.wait_for_click_available(FaqLocators.ORDER_BUTTON_FIN)
        self.click(FaqLocators.ORDER_BUTTON_FIN)
        self.wait_for_click_available(LocatorsOrder.ORDER_FORM)