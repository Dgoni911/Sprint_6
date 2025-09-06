from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    # Локаторы для вопросов о важном
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    FAQ_QUESTIONS = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton']")
    FAQ_ANSWERS = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel']")
    
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать'])[2]")
    
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[@href='/']")
    YANDEX_LOGO = (By.XPATH, "//a[@href='//yandex.ru']")
    
    def get_faq_question(self, index: int):
        questions = self.find_elements(self.FAQ_QUESTIONS)
        return questions[index]
    
    def get_faq_answer(self, index: int):
        answers = self.find_elements(self.FAQ_ANSWERS)
        return answers[index]
    
    def click_faq_question(self, index: int):
        question = self.get_faq_question(index)
        self.scroll_to_element(question)
        question.click()
    
    def get_faq_answer_text(self, index: int) -> str:
        answer = self.get_faq_answer(index)
        return answer.text
    
    def click_order_button_top(self):
        button = self.find_element(self.ORDER_BUTTON_TOP)
        self.scroll_to_element(button)
        button.click()
    
    def click_order_button_bottom(self):
        button = self.find_element(self.ORDER_BUTTON_BOTTOM)
        self.scroll_to_element(button)
        button.click()
    
    def click_scooter_logo(self):
        self.find_element(self.SCOOTER_LOGO).click()
    
    def click_yandex_logo(self):
        self.find_element(self.YANDEX_LOGO).click()