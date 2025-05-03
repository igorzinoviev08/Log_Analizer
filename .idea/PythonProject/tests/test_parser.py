from log_analyzer.parser import LogParser
from pathlib import Path

def test_parser(tmp_path):
    log_file = tmp_path / "test.log"
    log_file.write_text(
        "[2024-03-05 10:00:00] INFO django.requests: /api/v1/auth/login/\n"
        "[2024-03-05 10:00:01] ERROR django.requests: /admin/dashboard/\n"
    )
    parser = LogParser([log_file])
    data = parser.parse_all()
    assert len(data) == 2
    assert data[0]["handler"] == "/api/v1/auth/login/"
    assert data[0]["level"] == "INFO"
