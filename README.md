                **Структура проекта**

log_analyzer/
├── log_analyzer/
│   ├── __init__.py
│   ├── cli.py
│   ├── parser.py
│   ├── reporter.py
│   └── reports/
│       ├── __init__.py
│       ├── base.py
│       └── handlers.py
├── tests/
│   ├── __init__.py
│   ├── test_parser.py
│   ├── test_reporter.py
│   └── test_handlers_report.py
├── logs/
│   └── example.log  # Пример лога
├── pyproject.toml
├── pytest.ini
├── .gitignore
├── README.md
└── main.py

Основные компоненты 
✅ main.py — точка входа 

✅ cli.py — обработка командной строки

✅ parser.py — парсер логов

✅ reporter.py — фабрика отчётов

✅ reports/handlers.py — реализация отчёта handlers

✅ Базовый класс BaseReport

🧪 Тесты (pytest)

 📦 Зависимости (внутрь pyproject.toml или requirements.txt)

🚀 Как запускать


# Django Log Analyzer CLI

CLI-приложение для анализа логов Django и генерации отчётов.

## Установка

```bash
pip install -e .

## Использование
python main.py logs/app1.log logs/app2.log --report handlers

Добавление нового отчёта 

    Создайте новый файл в log_analyzer/reports/
    Унаследуйте класс от BaseReport
    Реализуйте методы build() и print_report()
    Зарегистрируйте его в REPORT_TYPES в reporter.py
     
 
