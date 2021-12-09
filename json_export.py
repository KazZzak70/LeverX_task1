from export import Exporter
import json
import pathlib
import room
import student


class JSONExporter(Exporter):

    @staticmethod
    def encode(any_obj):
        if isinstance(any_obj, (student.Student, room.Room)):
            return any_obj.to_dict()
        else:
            type_name = any_obj.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

    @staticmethod
    def export_file(data: list):
        output_file_path = pathlib.Path(pathlib.Path.cwd(), "output.json")
        with open(output_file_path, "w") as file:
            json.dump(data, file, default=JSONExporter.encode, indent="\t")
