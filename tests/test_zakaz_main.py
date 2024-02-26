import allure
import pytest
from constants import Constants
from pages.zakaz_main_page import ZakazMainPage
from pages.base_page import BasePage
from locators.locators_faq import FaqLocators


class TestZakazMain:
    @allure.title('Проверка входа в форму заказа через кнопку Заказать в футере')
    @allure.description(
        'Поиск кнопки Заказать скроллом и проверка корректного перехода в форму заказа')
    def test_bottom_order_button(self, driver):
        main_page = ZakazMainPage(driver)
        base_page = BasePage(driver)
        main_page.open_zakaz_main_page()
        main_page.scroll_to_button()
        assert base_page.current_url(driver) == Constants.ORDER_URL


    @allure.title('Проверка соответствия ответам на вопросы')
    @allure.description(
            'Поиск скроллом на странице блока вопросов, клик на каждый вопрос по очереди, проверка соответствия текста')
    @pytest.mark.parametrize(('answers', 'faq_q', 'faq_a'),
        [(Constants.FAQ_T_0, FaqLocators.FAQ_0_Q, FaqLocators.FAQ_0_A),
         (Constants.FAQ_T_1, FaqLocators.FAQ_1_Q, FaqLocators.FAQ_1_A),
         (Constants.FAQ_T_2, FaqLocators.FAQ_2_Q, FaqLocators.FAQ_2_A),
         (Constants.FAQ_T_3, FaqLocators.FAQ_3_Q, FaqLocators.FAQ_3_A),
         (Constants.FAQ_T_4, FaqLocators.FAQ_4_Q, FaqLocators.FAQ_4_A),
         (Constants.FAQ_T_5, FaqLocators.FAQ_5_Q, FaqLocators.FAQ_5_A),
         (Constants.FAQ_T_6, FaqLocators.FAQ_6_Q, FaqLocators.FAQ_6_A),
         (Constants.FAQ_T_7, FaqLocators.FAQ_7_Q, FaqLocators.FAQ_7_A)
         ])
    def test_faq_droprown_texts(self, driver, faq_q, faq_a, answers):
        base_page = ZakazMainPage(driver)
        main_page = ZakazMainPage(driver)
        main_page.open_zakaz_main_page()
        main_page.scroll_to_bottom()
        base_page.click(faq_q)
        assert base_page.text_extracting(faq_a) == answers

