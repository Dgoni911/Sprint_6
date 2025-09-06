import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature('Заказ самоката')
@allure.story('Позитивные сценарии заказа')
class TestOrder:
    
    ORDER_TEST_DATA = [
        {
            "test_name": "Заказ через верхнюю кнопку - черный самокат",
            "order_button": "top",
            "name": "Евгений",
            "lastname": "Косач",
            "address": "ул. Пушкина, д. ",
            "metro": "Сокольники",
            "phone": "+79181234567",
            "date": "25.12.2024",
            "rental_period": 0,
            "color": "black",
            "comment": "Позвонить за час до прибытия"
        },
        {
            "test_name": "Заказ через нижнюю кнопку - серый самокат",
            "order_button": "bottom",
            "name": "Ольга",
            "lastname": "Иванова",
            "address": "пр. Мира, д. 10, кв. 5",
            "metro": "Комсомольская",
            "phone": "+79187654321",
            "date": "26.12.2024",
            "rental_period": 1,
            "color": "grey",
            "comment": "Оставить у консьержа"
        }
    ]
    
    @allure.title('{test_name}')
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
            assert driver.current_url == main_page.base_url
    
    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.go_to_site()
        
        with allure.step('Запомнить текущее окно'):
            main_window = driver.current_window_handle
        
        with allure.step('Нажать на логотип Яндекса'):
            main_page.click_yandex_logo()
        
        with allure.step('Дождаться открытия нового окна'):
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            windows = driver.window_handles
            new_window = [window for window in windows if window != main_window][0]
            
            with allure.step('Переключиться на новое окно'):
                driver.switch_to.window(new_window)
                
                with allure.step('Проверить переход на Дзен'):
                    WebDriverWait(driver, 10).until(EC.url_contains('dzen.ru'))
                    assert 'dzen.ru' in driver.current_url.lower()
            
            with allure.step('Закрыть новое окно и вернуться'):
                driver.close()
                driver.switch_to.window(main_window)