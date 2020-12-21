# Тестовое задание (автотестирование)

## Использовал стек технологий:
- Selenium WD Python
- Pytest (тестовый framework)
- Allure (для вывода отчётов на странице в браузере)
- Тесты выполнены с применением паттерна PageObject

Драйверы браузеров вынесены в папку driver
<br>Папка allure-2.7.0 для запуска тестов с отчетом

Для создания allure отчётов использовать команду:
- pytest Tests.py --alluredir=allure_results (allures_results название папки где будут сохраненятся отчеты)

<br>Для просмотра отчетов использовать команду:
- allure serve allure_results

Для выбора браузера использовать команду:
- pytest —browser_name=firefox Tests.py
- pytest —browser_name=chrome Tests.py

Для запуска по умолчанию:
- pytest Tests.py

Использованные библиотеки находятся в файле requirements.txt 
