from source_func import dict_to_list
from serializer import Serializer
from room import Room
from student import Student
import xml.etree.ElementTree as ElTr
from pathlib import Path
import json


class JSONSerializer(Serializer):

    @staticmethod
    def encode(any_obj):
        if isinstance(any_obj, (Student, Room)):
            return any_obj.to_dict()
        else:
            type_name = any_obj.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

    @staticmethod
    def export_file(data: list, path: Path):
        output_file_path = Path(path, "output.json")
        with open(output_file_path, "w") as file:
            json.dump(data, file, default=JSONSerializer.encode, indent="\t")


class XMLSerializer(Serializer):

    @staticmethod
    def add_student(room: ElTr.SubElement, student_obj: Student):
        student = ElTr.SubElement(room, "student")
        student_id = ElTr.SubElement(student, "id")
        student_name = ElTr.SubElement(student, "name")
        student_id.text = str(student_obj.id)
        student_name.text = student_obj.name

    @staticmethod
    def add_room(root: ElTr.Element, room_obj: Room):
        room = ElTr.SubElement(root, "room")
        room_id = ElTr.SubElement(room, "id")
        room_name = ElTr.SubElement(room, "name")
        room_students = ElTr.SubElement(room, "students")
        room_id.text = str(room_obj.id)
        room_name.text = room_obj.name
        for student in room_obj.students:
            XMLSerializer.add_student(room_students, student)

    @staticmethod
    def export_file(data: list, path: Path):
        output_file_path = Path(path, "output.xml")
        root = ElTr.Element("rooms")
        for room in data:
            XMLSerializer.add_room(root=root, room_obj=room)
        tree = ElTr.ElementTree(root)
        tree.write(output_file_path, encoding="UTF-8", xml_declaration=True)


class SerializerFactory:

    @staticmethod
    def get_serializer(_format: str):
        if _format == "JSON":
            return JSONSerializer()
        elif _format == "XML":
            return XMLSerializer()
        else:
            raise ValueError(_format)


factory = SerializerFactory()


class HostelSerializer:

    @staticmethod
    def serialize(serializable, _format, path):
        serializer = factory.get_serializer(_format)
        return serializer.export_file(dict_to_list(serializable.rooms_dict), path)
