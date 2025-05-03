from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseReport(ABC):
    def __init__(self, raw_data: List[Dict[str, Any]]):
        self.raw_data = raw_data
        self._data = None

    @abstractmethod
    def build(self):
        ...

    @abstractmethod
    def print_report(self):
        ...
