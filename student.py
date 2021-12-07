from conversion import Conversion
from exceptions import InputFileError


class Student(Conversion):

    def __init__(self):
        self.id = None
        self.name = None
        self.room = None

    def __str__(self):
        return f"\nStudent {self.id}:\n\tName: {self.name}\n\tRoom: {self.room}"

    def to_dict(self):
        return {"id": self.id, "name": self.name}

    def initialize_from_dict(self, source_dict: dict):
        try:
            self.id = source_dict.get("id")
            self.name = source_dict.get("name")
            self.room = source_dict.get("room")
        except KeyError:
            raise InputFileError("Expected existence of fields: \"id\", \"name\", \"room\" in students source file")

    def settle(self, rooms_dict: dict):
        try:
            rooms_dict[self.room].students.append(self)
        except KeyError:
            raise InputFileError(f"There is no room with such id: {self.room}")
