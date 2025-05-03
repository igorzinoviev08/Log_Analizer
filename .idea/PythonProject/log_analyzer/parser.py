from pathlib import Path
from typing import Dict, Generator, List
import re

LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

class LogParser:
    def __init__(self, log_files: List[Path]):
        self.log_files = log_files
        self.handler_pattern = re.compile(r'.* (\w+) django.requests: (.*)$')

    def parse_all(self) -> List[Dict]:
        result = []
        for log_file in self.log_files:
            result.extend(self._parse_file(log_file))
        return result

    def _parse_file(self, path: Path) -> Generator[Dict, None, None]:
        with open(path, encoding='utf-8') as f:
            for line in f:
                if 'django.requests' in line:
                    parts = line.strip().split()
                    try:
                        level_index = parts.index('django.requests:') - 1
                        level = parts[level_index].upper()
                        handler = parts[-1]
                        if level in LOG_LEVELS:
                            yield {"handler": handler, "level": level}
                    except ValueError:
                        continue

