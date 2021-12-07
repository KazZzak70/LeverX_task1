from exceptions import InputFileError
from source_files_func import get_data, rooms_dict_to_list
from json_export import JSONExporter
from xml_export import XMLExporter
from student import Student
from room import Room

# /home/maksim/PycharmProjects/LeverX_task1/students.json
# /home/maksim/PycharmProjects/LeverX_task1/rooms.json


def main():
    students_file_path = "/home/maksim/PycharmProjects/LeverX_task1/students.json"
    rooms_file_path = "/home/maksim/PycharmProjects/LeverX_task1/rooms.json"

    students_source_data = get_data(file_path=students_file_path)
    rooms_source_data = get_data(file_path=rooms_file_path)

    students_list = []
    rooms_dict = dict()

    if rooms_source_data:
        for source_dict in rooms_source_data:
            room = Room()
            room.initialize_from_dict(source_dict)
            rooms_dict[source_dict["id"]] = room
    else:
        raise InputFileError("Expected data in source JSON file")

    if students_source_data:
        for source_dict in students_source_data:
            student = Student()
            student.initialize_from_dict(source_dict)
            student.settle(rooms_dict)
            students_list.append(student)
    else:
        raise InputFileError("Expected data in source JSON file")

    json_exporter = JSONExporter()
    json_exporter.export_json(data=rooms_dict_to_list(rooms_dict))
    xml_exporter = XMLExporter()
    xml_exporter.export_xml(data=rooms_dict_to_list(rooms_dict))


if __name__ == '__main__':
    main()

