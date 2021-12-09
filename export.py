from abc import ABC, abstractmethod


class Exporter(ABC):

    @staticmethod
    @abstractmethod
    def export_file(data: list):
        pass
