import pytest
import allure

@allure.feature('Простые тесты')
class TestSimple:
    
    @allure.title('Тест сложения')
    def test_addition(self):
        assert 1 + 1 == 2
    
    @allure.title('Тест строк')
    def test_string(self):
        assert "hello".upper() == "HELLO"
