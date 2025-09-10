import pytest
import allure
from pages.main_page import MainPage
from data import FAQ_TEST_DATA  

@allure.feature('FAQ раздел')
@allure.story('Проверка выпадающего списка вопросов')
class TestFAQ:
    
    @allure.title('Проверка ответа на вопрос №{question_index + 1}')
    @pytest.mark.parametrize('question_index, expected_answer', FAQ_TEST_DATA)
    def test_faq_question_answer(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.go_to_site()
        
        with allure.step(f'Кликнуть на вопрос №{question_index + 1}'):
            main_page.click_faq_question(question_index)
        
        with allure.step('Проверить текст ответа'):
            actual_answer = main_page.get_faq_answer_text(question_index)
            assert actual_answer == expected_answer, \
                f"Ожидаемый ответ: '{expected_answer}', Фактический: '{actual_answer}'"