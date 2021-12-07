from abc import ABC, abstractmethod


class Conversion(ABC):

    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def initialize_from_dict(self, source_dict: dict):
        pass
