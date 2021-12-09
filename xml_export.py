from student import Student
from room import Room
from export import Exporter
import xml.etree.ElementTree as ElTr


class XMLExporter(Exporter):

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
            XMLExporter.add_student(room_students, student)

    @staticmethod
    def export_file(data: list):
        root = ElTr.Element("rooms")
        for room in data:
            XMLExporter.add_room(root=root, room_obj=room)
        tree = ElTr.ElementTree(root)
        tree.write("output.xml", encoding="UTF-8", xml_declaration=True)
