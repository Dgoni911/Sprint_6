from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from config import BASE_URL
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL  
    
    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator: tuple, time: int = 10) -> WebElement:
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )
    
    @allure.step("Найти элементы по локатору: {locator}")
    def find_elements(self, locator: tuple, time: int = 10) -> list[WebElement]:
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )
    
    @allure.step("Перейти на сайт")
    def go_to_site(self):
        self.driver.get(self.base_url)
    
    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_element_visible(self, locator: tuple, time: int = 10) -> WebElement:
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Element {locator} not visible"
        )
    
    @allure.step("Скролл к элементу")
    def scroll_to_element(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step("Кликнуть по элементу")
    def click_element(self, element: WebElement):
        element.click()
    
    @allure.step("Ввести текст '{text}' в элемент")
    def input_text(self, element: WebElement, text: str):
        element.clear()
        element.send_keys(text)
    
    # НОВЫЕ МЕТОДЫ ДЛЯ РАБОТЫ С test_order.py
    
    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.driver.current_url
    
    @allure.step("Проверить что текущий URL равен {expected_url}")
    def check_current_url(self, expected_url: str) -> bool:
        return self.get_current_url() == expected_url
    
    @allure.step("Дождаться количества окон: {number}")
    def wait_for_number_of_windows(self, number: int, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(number)
        )
    
    @allure.step("Получить handles всех окон")
    def get_window_handles(self):
        return self.driver.window_handles
    
    @allure.step("Переключиться на окно: {window_handle}")
    def switch_to_window(self, window_handle: str):
        self.driver.switch_to.window(window_handle)
    
    @allure.step("Дождаться что URL содержит: {text}")
    def wait_for_url_contains(self, text: str, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )
    
    @allure.step("Проверить что URL содержит: {text}")
    def check_url_contains(self, text: str) -> bool:
        return text in self.get_current_url().lower()
    
    @allure.step("Получить текущий handle окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    @allure.step("Проверить отображение элемента")
    def is_element_displayed(self, locator: tuple) -> bool:
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False