from abc import ABC, abstractmethod
from typing import Any

class Database(ABC):
    @abstractmethod
    def get(self, key: Any, *args, **kwargs) -> Any:
        pass
    @abstractmethod
    def put(self, key: Any, value: Any, *args, **kwargs) -> Any:
        pass