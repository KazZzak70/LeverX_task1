from exceptions import InputFileError
from pathlib import Path
import json


def json_file_exists(path: Path) -> bool:
    return True if (path.exists() and path.suffix == ".json") else False


def get_data(file: Path):
    if json_file_exists(file):
        with open(file) as file:
            data_list = json.load(file)
        return data_list
    else:
        raise InputFileError("Check the input file path/type")


def dict_to_list(source_dict: dict) -> list:
    return list(source_dict.values())
