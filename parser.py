import pathlib
import json

path = pathlib.PurePath(__file__).parent

with open('info.json', 'r') as f:
    inf = json.load(f)


print(inf['days'][0])

for k in inf['days']:
    pass
    # print(k['date'])
