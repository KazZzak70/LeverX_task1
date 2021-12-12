import argparse
import pathlib


def configure_parser():
    parser = argparse.ArgumentParser(description="Student Data Serializer")
    parser.add_argument("students_file_path", help="Path to students source file")
    parser.add_argument("rooms_file_path", help="Path to rooms source file")
    parser.add_argument("--to-xml", dest="output_formats", help="Export result to .xml file format",
                        action="append_const", const="XML")
    parser.add_argument("--to-json", dest="output_formats", help="Export result to .json file format",
                        action="append_const", const="JSON")
    parser.add_argument("--to-path", help="Setting the output path for files",
                        default=str(pathlib.Path.cwd()))
    return parser
