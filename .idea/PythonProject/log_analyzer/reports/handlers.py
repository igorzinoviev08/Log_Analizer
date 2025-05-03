from collections import defaultdict
from typing import List, Dict, Any
from log_analyzer.reports.base import BaseReport

LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']


class HandlersReport(BaseReport):
    def build(self) -> None:
        self._data = defaultdict(lambda: {level: 0 for level in LOG_LEVELS})
        total_row = {level: 0 for level in LOG_LEVELS}

        for entry in self.raw_data:
            handler = entry["handler"]
            level = entry["level"]

            if level in LOG_LEVELS:
                self._data[handler][level] += 1
                total_row[level] += 1

        self._total_row = total_row

    def print_report(self) -> None:
        total_requests = sum(self._total_row.values())
        print(f"Total requests: {total_requests}\n")

        headers = ["HANDLER"] + LOG_LEVELS
        column_widths = {
            "HANDLER": max(max(len(handler) for handler in self._data), len("HANDLER")),
            **{level: max(
                max(len(str(self._data[handler][level])) for handler in self._data),
                len(level)
            ) for level in LOG_LEVELS}
        }

        def format_row(parts):
            return "  ".join(str(part).ljust(column_widths[key]) for key, part in parts.items())

        print(format_row(dict(zip(headers, headers))))

        for handler in sorted(self._data):
            row = {"HANDLER": handler}
            row.update({level: self._data[handler][level] for level in LOG_LEVELS})
            print(format_row(row))

        total_line = {"HANDLER": ""}
        total_line.update({level: self._total_row[level] for level in LOG_LEVELS})
        print(format_row(total_line))
