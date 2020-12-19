# Тестовое задание (автотестирование)

## Использовал стек технологий:
- Selenium WD Python
- Pytest (тестовый framework)
- Allure (для вывода отчётов на странице в браузере)
Тесты выполнены с применением PageObject паттерн

Драйверы браузеров вынесены в папку driver
Папка allure-2.7.0 для запуска тестов с отчетом

Для создания allure отчётов использовать команду:
pytest Tests.py 
- --alluredir=allure_results (где =allures_results название папки для сохранения отчетов)
Для просмотра отчетов использовать команду:
- allure serve allure_results

Для выбора браузера использовать команду:
- pytest —browser_name=firefox Tests.py
- pytest —browser_name=chrome Tests.py

Использованные библиотеки находятся в файле requirements.txt 
