 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
⌄
⌄
⌄
⌄
# Django Log Analyzer CLI

CLI-приложение для анализа логов Django и генерации отчётов.

## Описание

Это консольное приложение анализирует логи Django-приложения и формирует отчёты.  
Поддерживает работу с несколькими файлами и позволяет легко добавлять новые типы отчётов.

---

## 🧩 Функционал

- Поддержка нескольких файлов логов
- Отчёт `handlers`: количество запросов по ручкам и уровням логирования
- Проверка существования файлов
- Расширяемая архитектура под новые типы отчётов

---

## 📁 Структура проекта

 
 

log_analyzer/
├── main.py                   # Точка входа
├── log_analyzer/
│   ├── init .py
│   ├── cli.py                # Обработка аргументов командной строки
│   ├── parser.py             # Парсинг логов
│   └── reporter.py           # Логика формирования отчётов
│   └── reports/
│       ├── init .py
│       └── handlers.py       # Реализация отчёта "handlers"
├── tests/                    # Тесты (pytest)
├── logs/                     # Примеры логов
├── README.md
├── pyproject.toml
├── pytest.ini
└── .gitignore 
 
 
1
2
3
4
5
6
7

---

## ⚙️ Установка

```bash
pip install -e .
 
 
🚀 Использование 
bash
 
 
1
python main.py logs/app1.log logs/app2.log --report handlers
 
 

Пример вывода: 
 
 
1
2
3
4
5
6
7
Total requests: 4

HANDLER               	DEBUG  	INFO   	WARNING	ERROR  	CRITICAL  
/api/v1/auth/login/     	1     		1      	0      		0      		0   	 
/admin/dashboard/       	0     		0      	0      		1      		0   	 
/api/v1/orders/         	0     		1      	0      		0      		0   	 
                            1    		2      	0      		1      		0   
 
 
🧪 Запуск тестов 
bash
 
 
1
pytest --cov=log_analyzer tests/
 
 
🧱 Архитектура 

Проект использует ООП и расширяемую систему отчётов: 

    BaseReport — абстрактный класс для всех отчётов
    HandlersReport — реализация конкретного отчёта
    Reporter — фабрика отчётов
    LogParser — парсер логов
     

Добавление нового отчёта требует только создания нового класса в папке reports/. 
✅ Лицензия 

MIT License  
