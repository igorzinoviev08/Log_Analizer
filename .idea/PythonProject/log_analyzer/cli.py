import argparse
from pathlib import Path
from typing import List

from log_analyzer.parser import LogParser
from log_analyzer.reporter import Reporter


def run_cli() -> None:
    parser = argparse.ArgumentParser(description="Log analyzer for Django applications")
    parser.add_argument("log_paths", nargs="+", type=str, help="Paths to log files")
    parser.add_argument("--report", required=True, choices=["handlers"], help="Type of report to generate")

    args = parser.parse_args()

    log_files: List[Path] = [Path(p) for p in args.log_paths]
    report_type: str = args.report

    # Проверяем существование файлов
    for log_file in log_files:
        if not log_file.exists():
            raise FileNotFoundError(f"Log file not found: {log_file}")

    # Обрабатываем логи
    parser_instance = LogParser(log_files)
    data = parser_instance.parse_all()

    # Формируем отчет
    reporter = Reporter(data)
    reporter.generate(report_type)
