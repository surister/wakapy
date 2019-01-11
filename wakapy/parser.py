import pathlib
import json
from typing import List

from wakapy.days import Day

path = pathlib.PurePath(__file__).parent


class JsonFile:
    def __init__(self, fp: str):
        self.fp = fp
        self.file = self.load_file()
        self._days = [Day(item) for item in self.file['days']]

        Day(self.file['days'][0])

    def load_file(self) -> dict:
        with open(self.fp, 'r') as f:
            a = json.load(f)
            return a

    @property
    def user_info(self) -> dict:
        return self.file['user']

    @property
    def days(self) -> List[Day]:
        return self._days

    def __repr__(self):
        return f'Wakapy.{self.__class__.__name__}({self.fp})'
