from student import Student
from room import Room
from export import Exporter
import xml.etree.ElementTree as XML


class XMLExporter(Exporter):

    @staticmethod
    def add_student(room: XML.SubElement, student_obj: Student):
        student = XML.SubElement(room, "student")
        student_id = XML.SubElement(student, "id")
        student_name = XML.SubElement(student, "name")
        student_id.text = str(student_obj.id)
        student_name.text = student_obj.name

    def add_room(self, root: XML.Element, room_obj: Room):
        room = XML.SubElement(root, "room")
        room_id = XML.SubElement(room, "id")
        room_name = XML.SubElement(room, "name")
        room_students = XML.SubElement(room, "students")
        room_id.text = str(room_obj.id)
        room_name.text = room_obj.name
        for student in room_obj.students:
            self.add_student(room_students, student)

    def export_xml(self, data: list):
        root = XML.Element("rooms")
        for room in data:
            self.add_room(root=root, room_obj=room)
        tree = XML.ElementTree(root)
        tree.write("output.xml", encoding="UTF-8", xml_declaration=True)
