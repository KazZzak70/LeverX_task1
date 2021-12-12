from exceptions import InputFileError


class Student:

    def __init__(self, id: int, name: str, room: int, *args, **kwargs):
        self.id = id
        self.name = name
        self.room = room

    def __str__(self):
        return f"\nStudent {self.id}:\n\tName: {self.name}\n\tRoom: {self.room}"

    def to_dict(self):
        return {"id": self.id, "name": self.name}
