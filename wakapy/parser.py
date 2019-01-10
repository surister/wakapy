import pathlib
import json

from wakapy.days import Day

path = pathlib.PurePath(__file__).parent


class JsonFile:
    def __init__(self, fp: str):
        self.fp = fp
        self.file = self.load_file()
        #self._days = [Day(item) for item in self.file['days']]
        #self.test = Day([self.file['days']])

        Day(self.file['days'][0])

    def load_file(self):
        with open(self.fp, 'r') as f:
            return json.load(f)

    @property
    def user_info(self) -> dict:
        return self.file['user']

    @property
    def days(self):
        return self._days

    def test(self):
        return self.file['days']


if __name__ == '__main__':
    a = JsonFile(r'C:\Users\k260g\Desktop\project\info.json')