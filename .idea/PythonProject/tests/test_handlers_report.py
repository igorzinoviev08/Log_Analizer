from log_analyzer.reports.handlers import HandlersReport

sample_data = [
    {"handler": "/api/v1/auth/login/", "level": "INFO"},
    {"handler": "/admin/dashboard/", "level": "ERROR"},
    {"handler": "/api/v1/auth/login/", "level": "INFO"},
]

def test_handlers_report_counts():
    report = HandlersReport(sample_data)
    report.build()
    assert report._data["/api/v1/auth/login/"]["INFO"] == 2
    assert report._data["/admin/dashboard/"]["ERROR"] == 1
