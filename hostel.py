from exceptions import InputFileError
from student import Student
from room import Room


class Hostel:

    def __init__(self):
        self.students_list: list[Student] = []
        self.rooms_dict: dict = {}

    def load_students(self, data: list[dict]):
        if data:
            for data_dict in data:
                student = Student(**data_dict)
                self.settle_student(student)
                self.students_list.append(student)
        else:
            raise InputFileError("Expected data in students source JSON file")

    def load_rooms(self, data: list[dict]):
        if data:
            for data_dict in data:
                room = Room(**data_dict)
                self.rooms_dict[room.id] = room
        else:
            raise InputFileError("Expected data in source JSON file")

    def settle_student(self, student: Student):
        self.rooms_dict[student.room].students.append(student)

