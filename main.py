from args import configure_parser
from exceptions import InputFileError
from source_files_func import get_data, rooms_dict_to_list
from json_export import JSONExporter
from xml_export import XMLExporter
from student import Student
from room import Room


def main():
    args = configure_parser().parse_args()

    students_data = get_data(file_path=args.students_file_path)
    rooms_data = get_data(file_path=args.rooms_file_path)

    students_list = []
    rooms_dict = dict()

    if rooms_data:
        for source_dict in rooms_data:
            room = Room()
            room.initialize_from_dict(source_dict)
            rooms_dict[source_dict["id"]] = room
    else:
        raise InputFileError("Expected data in source JSON file")

    if students_data:
        for source_dict in students_data:
            student = Student()
            student.initialize_from_dict(source_dict)
            student.settle(rooms_dict)
            students_list.append(student)
    else:
        raise InputFileError("Expected data in source JSON file")

    if args.to_xml:
        XMLExporter.export_file(data=rooms_dict_to_list(rooms_dict))
    if args.to_json:
        JSONExporter.export_file(data=rooms_dict_to_list(rooms_dict))


if __name__ == '__main__':
    main()
