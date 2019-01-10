import pathlib
import json

path = pathlib.PurePath(__file__).parent


class Injector:
    @staticmethod
    def _user_info_extractor(fp: str):
        with open(fp, 'r') as f:
            inf = json.load(f)
        return inf['user']

    def info(self, fp):
        return self._user_info_extractor(fp)
