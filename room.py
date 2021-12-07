from conversion import Conversion
from exceptions import InputFileError


class Room(Conversion):

    def __init__(self):
        self.id = None
        self.name = None
        self.students = []

    def __str__(self):
        return f"\nRoom {self.id}:\n\tName: {self.name}"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "students": self.students}

    def initialize_from_dict(self, source_dict: dict):
        try:
            self.id = source_dict.get("id")
            self.name = source_dict.get("name")
        except KeyError:
            raise InputFileError("Expected existence of fields: \"id\", \"name\" in rooms source file")
