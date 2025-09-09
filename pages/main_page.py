from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class MainPage(BasePage):
    # Локаторы для вопросов о важном
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemButton']")
    FAQ_ANSWERS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel']")
    
    # Кнопки заказа 
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM:last-of-type")
    
    # Или
    ORDER_BUTTON = (By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    
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
        # Используем первый найденный элемент 
        buttons = self.find_elements(self.ORDER_BUTTON)
        if buttons:
            self.scroll_to_element(buttons[0])
            buttons[0].click()
        else:
            raise Exception("Order button not found")
    
    @allure.step("Кликнуть нижнюю кнопку заказа")
    def click_order_button_bottom(self):
        # Используем последний найденный элемент
        buttons = self.find_elements(self.ORDER_BUTTON)
        if buttons and len(buttons) > 1:
            self.scroll_to_element(buttons[-1])
            buttons[-1].click()
        else:
            raise Exception("Bottom order button not found")
    
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