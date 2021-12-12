from abc import ABC, abstractmethod
from pathlib import Path


class Serializer(ABC):

    @staticmethod
    @abstractmethod
    def export_file(data: list, path: Path):
        pass
