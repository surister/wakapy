from pathlib import PurePath, Path
from typing import NamedTuple


def order_dict(_dict, reverse=True):
    temp_dict = {}

    unordered_list = [(k, v) for k, v in _dict.items()]
    ordered_list = sorted(unordered_list, key=lambda x: x[1] , reverse=reverse)

    for item in ordered_list:
        temp_dict[item[0]] = item[1]

    return temp_dict


class Constants(NamedTuple):
    data_path = PurePath(PurePath(__file__).parent).joinpath('data/')
    data_files = [file for file in Path(data_path).iterdir()]

