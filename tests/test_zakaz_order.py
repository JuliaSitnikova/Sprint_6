import allure
from pages.zakaz_main_page import ZakazMainPage
from pages.zakaz_order_page import ZakazOrderPage



class TestZakazOrder:
    @allure.title('Проверка корректного заполнения формы заказа')  # декораторы
    @allure.description(
        'Открытие страницы, переход в форму заказа, заполнение данными, ожидание формы успешного заказа')
    def test_bottom_order_button(self, driver):
        order_page = ZakazOrderPage(driver)
        main_page = ZakazMainPage(driver)
        main_page.open_zakaz_main_page()
        main_page.scroll_to_button()
        order_page.fill_order_form()
        order_page.fill_rent_form()
        assert 'Заказ оформлен' in order_page.get_confirmation_window_header()
