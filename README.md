# Sprint_6: Автотесты для Яндекс.Самокат

## Описание
Проект автотестов для учебного сервиса "Яндекс.Самокат" с использованием:
- Selenium WebDriver
- Pytest
- Allure Reports
- Page Object Pattern

## Установка
```bash
pip install -r requirements.txt
```

## Запуск тестов
```bash
# Все тесты
pytest tests/ --alluredir=allure_results

# Генерация отчета
allure serve allure_results
```

## Структура проекта
- `pages/` - Page Object классы
- `tests/` - Тесты
- `allure_results/` - Allure отчеты
