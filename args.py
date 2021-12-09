import argparse


def configure_parser():
    parser = argparse.ArgumentParser(description="Student Data Converter")
    parser.add_argument("students_file_path", help="Path to students source file")
    parser.add_argument("rooms_file_path", help="Path to rooms source file")
    parser.add_argument("--to-xml", help="Export result to .xml file format", action="store_true")
    parser.add_argument("--to-json", help="Export result to .json file format", action="store_true")
    return parser
