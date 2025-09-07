from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"
    
    def find_element(self, locator: tuple, time: int = 10) -> WebElement:
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )
    
    def find_elements(self, locator: tuple, time: int = 10) -> list[WebElement]:
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )
    
    def go_to_site(self):
        self.driver.get(self.base_url)
    
    def wait_for_element_visible(self, locator: tuple, time: int = 10) -> WebElement:
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Element {locator} not visible"
        )
    
    def scroll_to_element(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)