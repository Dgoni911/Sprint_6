import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_TEST_DATA

@allure.feature('Заказ самоката')
@allure.story('Позитивные сценарии заказа')
class TestOrder:
    
    @allure.title('{order_data[test_name]}')
    @pytest.mark.parametrize('order_data', ORDER_TEST_DATA)
    def test_order_scooter_positive(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.go_to_site()
        
        with allure.step(f'Нажать кнопку "Заказать" ({order_data["order_button"]})'):
            if order_data["order_button"] == "top":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()
        
        with allure.step('Заполнить форму личной информации'):
            order_page.fill_personal_info(
                order_data["name"],
                order_data["lastname"],
                order_data["address"],
                order_data["metro"],
                order_data["phone"]
            )
        
        with allure.step('Заполнить форму аренды'):
            order_page.fill_rental_info(
                order_data["date"],
                order_data["rental_period"],
                order_data["color"],
                order_data["comment"]
            )
        
        with allure.step('Проверить успешное оформление заказа'):
            assert order_page.is_success_modal_displayed(), \
                "Модальное окно успешного заказа не отображается"
    
    @allure.title('Проверка перехода по логотипу Самоката')
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.go_to_site()
        
        with allure.step('Нажать на логотип Самоката'):
            main_page.click_scooter_logo()
        
        with allure.step('Проверить переход на главную страницу'):
            assert main_page.check_current_url(main_page.base_url), \
                "Не произошел переход на главную страницу после клика по логотипу Самоката"
    
    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.go_to_site()
        
        with allure.step('Нажать на логотип Яндекса'):
            main_page.click_yandex_logo()
        
        with allure.step('Дождаться открытия нового окна и проверить переход на Дзен'):
            main_page.wait_for_number_of_windows(2)
            windows = main_page.get_window_handles()
            
            # Переключаемся на новое окно
            main_page.switch_to_window(windows[-1])
            
            # Проверяем переход на Дзен
            main_page.wait_for_url_contains('dzen.ru')
            assert main_page.check_url_contains('dzen.ru'), \
                "Не произошел переход на Дзен после клика по логотипу Яндекса"