from typing import List, Dict
from log_analyzer.reports.handlers import HandlersReport

REPORT_TYPES = {
    "handlers": HandlersReport,
}

class Reporter:
    def __init__(self, data: List[Dict]):
        self.data = data

    def generate(self, report_type: str) -> None:
        report_class = REPORT_TYPES.get(report_type)
        if not report_class:
            raise ValueError(f"Unknown report type: {report_type}")
        report = report_class(self.data)
        report.build()
        report.print_report()
