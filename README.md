# Sprint_6 
Проект автоматизации тестирования 
 
## Установка 
\`pip install -r requirements.txt\` 
 
## Запуск тестов 
\`pytest tests/ --alluredir=allure_results -v\` 
 
## Генерация отчета Allure 
\`allure serve allure_results\` 
 
## Структура проекта 
- \`pages/\` - Page Object модели 
- \`tests/\` - Тесты 
- \`conftest.py\` - Фикстуры pytest 
