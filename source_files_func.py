from exceptions import InputFileError
import pathlib
import json


def json_file_exists(path: pathlib.Path) -> bool:
    return True if (path.exists() and path.suffix == ".json") else False


def get_data(file_path: str):
    file_path = pathlib.Path(file_path)
    if json_file_exists(file_path):
        with open(file_path) as file:
            data_list = json.load(file)
        return data_list
    else:
        raise InputFileError("Check the input file path/type")


def rooms_dict_to_list(source_dict: dict) -> list:
    rooms_list = [item[1] for item in source_dict.items()]
    return rooms_list

