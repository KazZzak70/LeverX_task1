from serializers import HostelSerializer
from pathlib import Path
from source_func import get_data, dict_to_list
from args import configure_parser
from hostel import Hostel

# /home/maksim/PycharmProjects/LeverX_task1/students.json
# /home/maksim/PycharmProjects/LeverX_task1/rooms.json


def main():
    args = configure_parser().parse_args()
    output_path = Path(args.to_path)

    hostel = Hostel()

    rooms_file = Path(args.rooms_file_path)
    rooms_data = get_data(file=rooms_file)
    hostel.load_rooms(rooms_data)

    students_file = Path(args.students_file_path)
    students_data = get_data(file=students_file)
    hostel.load_students(students_data)

    serializer = HostelSerializer()
    for _format in args.output_formats:
        serializer.serialize(hostel, _format, output_path)


if __name__ == '__main__':
    main()
