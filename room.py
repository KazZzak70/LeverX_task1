class Room:

    def __init__(self, id: int, name: str, *args, **kwargs):
        self.id = id
        self.name = name
        self.students = []

    def __str__(self):
        return f"\nRoom {self.id}:\n\tName: {self.name}"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "students": self.students}
