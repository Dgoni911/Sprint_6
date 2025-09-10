from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class MainPage(BasePage):
    # Локаторы для вопросов о важном
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemButton']")
    FAQ_ANSWERS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel']")
    
    # Кнопки заказа 
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Home_Header')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    
    # Логотипы
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    
    @allure.step("Получить вопрос FAQ по индексу {index}")
    def get_faq_question(self, index: int):
        questions = self.find_elements(self.FAQ_QUESTIONS)
        if index < len(questions):
            return questions[index]
        raise IndexError(f"FAQ question index {index} out of range")
    
    @allure.step("Получить ответ FAQ по индексу {index}")
    def get_faq_answer(self, index: int):
        answers = self.find_elements(self.FAQ_ANSWERS)
        if index < len(answers):
            return answers[index]
        raise IndexError(f"FAQ answer index {index} out of range")
    
    @allure.step("Кликнуть на вопрос FAQ с индексом {index}")
    def click_faq_question(self, index: int):
        question = self.get_faq_question(index)
        self.scroll_to_element(question)
        question.click()
    
    @allure.step("Получить текст ответа FAQ с индексом {index}")
    def get_faq_answer_text(self, index: int) -> str:
        answer = self.get_faq_answer(index)
        return answer.text
    
    @allure.step("Кликнуть верхнюю кнопку заказа")
    def click_order_button_top(self):
        button = self.find_element(self.ORDER_BUTTON_TOP)
        self.scroll_to_element(button)
        button.click()
    
    @allure.step("Кликнуть нижнюю кнопку заказа")
    def click_order_button_bottom(self):
        button = self.find_element(self.ORDER_BUTTON_BOTTOM)
        self.scroll_to_element(button)
        button.click()
    
    @allure.step("Нажать кнопку заказа: {button_type}")
    def click_order_button(self, button_type: str):
        if button_type == "top":
            self.click_order_button_top()
        else:
            self.click_order_button_bottom()
    
    @allure.step("Кликнуть логотип Самоката")
    def click_scooter_logo(self):
        self.find_element(self.SCOOTER_LOGO).click()
    
    @allure.step("Кликнуть логотип Яндекса")
    def click_yandex_logo(self):
        self.find_element(self.YANDEX_LOGO).click()
    
    @allure.step("Проверить видимость секции FAQ")
    def is_faq_section_visible(self) -> bool:
        try:
            return self.find_element(self.FAQ_SECTION).is_displayed()
        except:
            return False