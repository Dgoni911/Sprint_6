from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from .base_page import BasePage

class OrderPage(BasePage):
    # Форма заказа - шаг 1
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[@class='select-search__select']//li")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Форма заказа - шаг 2
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-root')]")
    RENTAL_PERIOD_OPTIONS = (By.XPATH, "//div[@class='Dropdown-option']")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    # Модальное окно успеха
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]//div[contains(@class, 'Order_Text__2broi')]")
    
    def fill_personal_info(self, name: str, lastname: str, address: str, metro_station: str, phone: str):
        self.find_element(self.NAME_INPUT).send_keys(name)
        self.find_element(self.LASTNAME_INPUT).send_keys(lastname)
        self.find_element(self.ADDRESS_INPUT).send_keys(address)
        
        # Выбор станции метро
        self.find_element(self.METRO_INPUT).click()
        stations = self.find_elements(self.METRO_STATION_OPTION)
        for station in stations:
            if metro_station in station.text:
                station.click()
                break
        
        self.find_element(self.PHONE_INPUT).send_keys(phone)
        self.find_element(self.NEXT_BUTTON).click()
    
    def fill_rental_info(self, date: str, rental_period: int, color: str, comment: str):
        # Дата доставки
        self.find_element(self.DATE_INPUT).send_keys(date)
        
        # Период аренды
        self.find_element(self.RENTAL_PERIOD_DROPDOWN).click()
        periods = self.find_elements(self.RENTAL_PERIOD_OPTIONS)
        periods[rental_period].click()
        
        # Цвет самоката
        if color == "black":
            self.find_element(self.COLOR_BLACK_CHECKBOX).click()
        elif color == "grey":
            self.find_element(self.COLOR_GREY_CHECKBOX).click()
        
        # Комментарий
        if comment:
            self.find_element(self.COMMENT_INPUT).send_keys(comment)
        
        # Заказ
        self.find_element(self.ORDER_BUTTON).click()
        self.find_element(self.CONFIRM_BUTTON).click()
    
    def is_success_modal_displayed(self) -> bool:
        try:
            return self.find_element(self.SUCCESS_MODAL, time=5).is_displayed()
        except:
            return False
    
    def get_success_message(self) -> str:
        return self.find_element(self.SUCCESS_MESSAGE).text