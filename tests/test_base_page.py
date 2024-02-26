import allure
from constants import Constants
from pages.base_page import BasePage
from pages.zakaz_main_page import ZakazMainPage



class TestBasePage:

    @allure.title('Проверка входа в форму заказа через кнопку в хэдере')
    @allure.description(
        'Поиск кнопки Заказать и проверка корректного перехода в форму заказа')
    def test_upper_order_button(self, driver):
        main_page = ZakazMainPage(driver)
        base_page = BasePage(driver)
        main_page.open_zakaz_main_page()
        main_page.order_button_click()
        assert base_page.current_url(driver) == Constants.ORDER_URL

    @allure.title('Проверка возврата на главную страницу при клике на логотип Самокат')
    @allure.description(
        'Переход в форму заказа, клик на логотип Самокат, проверка корректноного перехода на главную страницу')
    def test_redirect_to_main_from_order(self, driver):
        main_page = ZakazMainPage(driver)
        base_page = BasePage(driver)
        main_page.open_zakaz_main_page()
        main_page.order_button_click()
        main_page.samokat_logo_click()
        assert base_page.current_url(driver) == Constants.MAIN_URL

    @allure.title('Проверка возврата на главную страницу при клике на логотип Самокат')
    @allure.description(
        'Переход в форму заказа, клик на логотип Самокат, проверка корректноного перехода на главную страницу')
    def test_redirect_to_dzen_from_order(self, driver):
        main_page = ZakazMainPage(driver)
        base_page = BasePage(driver)
        main_page.open_zakaz_main_page()
        main_page.logo_to_dzen()
        assert base_page.url_partition(driver) == Constants.DZEN_URL