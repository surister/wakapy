import json
from typing import List

from wakapy.days import Day


class JsonFile:
    def __init__(self, fp: str):
        self.fp = fp
        self.file = self._load_file()
        self._days = [Day(item) for item in self.file['days']]

        Day(self.file['days'][0])

    def _load_file(self) -> dict:
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
        return f"<'wakapy.{self.__class__.__name__}({self.fp})'>"
