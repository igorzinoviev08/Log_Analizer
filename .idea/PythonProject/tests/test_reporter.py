import pytest
from log_analyzer.reporter import Reporter
from log_analyzer.reports.handlers import HandlersReport


@pytest.fixture
def sample_data():
    return [
        {"handler": "/api/v1/auth/login/", "level": "INFO"},
        {"handler": "/admin/dashboard/", "level": "ERROR"},
        {"handler": "/api/v1/auth/login/", "level": "DEBUG"},
    ]


def test_reporter_generates_handlers_report(sample_data):
    reporter = Reporter(sample_data)
    with pytest.raises(NotImplementedError):
        # Проверяем, что базовый метод generate вызывает NotImplementedError
        reporter.generate("unknown_report_type")

    # Переопределяем REPORT_TYPES только для теста
    from log_analyzer.reporter import REPORT_TYPES
    original_handlers = REPORT_TYPES["handlers"]
    try:
        REPORT_TYPES["handlers"] = type('MockHandlersReport', (HandlersReport,), {
            'build': lambda self: None,
            'print_report': lambda self: None
        })

        mock_report_instance = REPORT_TYPES["handlers"](sample_data)
        mock_report_instance.build()
        mock_report_instance.print_report()

        reporter.generate("handlers")  # Не должно быть ошибок

    finally:
        # Восстанавливаем оригинальный класс
        REPORT_TYPES["handlers"] = original_handlers


def test_reporter_raises_for_unknown_report_type(sample_data):
    reporter = Reporter(sample_data)
    with pytest.raises(ValueError):
        reporter.generate("non_existing_report")
