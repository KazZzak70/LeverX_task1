from abc import ABC


class Exporter(ABC):

    def export_json(self, data: list[dict]):
        pass

    def export_xml(self, data: list):
        pass
