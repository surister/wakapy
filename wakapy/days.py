

class Day:
    def __init__(self, _dict):
        print(_dict)
        self.name = _dict.get('name')
        self.date = _dict.get('date')

    def __repr__(self):
        return f'{self.__class__.__name__}{self.date}'

a = {
    'categories':
    [
        {'digital': '0:05:20', 'hours': 0, 'minutes': 5, 'name': 'Coding', 'percent': 100.0, 'seconds': 20, 'text': '5 mins', 'total_seconds': 320}

         ],
    'date': '2018-08-02',
    'dependencies':
        [
            {'digital': '0:05:15', 'hours': 0, 'minutes': 5, 'name': 'discord', 'percent': 33.51, 'seconds': 15, 'text': '5 mins', 'total_seconds': 315},
            {'digital': '0:05:12', 'hours': 0, 'minutes': 5, 'name': 'Bot', 'percent': 33.19, 'seconds': 12, 'text': '5 mins', 'total_seconds': 312},
            {'digital': '0:05:08', 'hours': 0, 'minutes': 5, 'name': 'time', 'percent': 32.77, 'seconds': 8, 'text': '5 mins', 'total_seconds': 308},
            {'digital': '0:00:05', 'hours': 0, 'minutes': 0, 'name': 'json', 'percent': 0.53, 'seconds': 5, 'text': '5 secs', 'total_seconds': 5},
            {'digital': '0:00:00', 'hours': 0, 'minutes': 0, 'name': 'requests', 'percent': 0.0, 'seconds': 0, 'text': '0 secs', 'total_seconds': 0}
        ],
    'editors': [
        {'digital': '0:05:20', 'hours': 0, 'minutes': 5, 'name': 'PyCharmCore', 'percent': 100.0, 'seconds': 20, 'text': '5 mins', 'total_seconds': 320}
    ],
    'grand_total':
        {'digital': '0:05', 'hours': 0, 'minutes': 5, 'text': '5 mins', 'total_seconds': 320},
    'languages':
        [
        {'digital': '0:05:20', 'hours': 0, 'minutes': 5, 'name': 'Python', 'percent': 100.0, 'seconds': 20, 'text': '5 mins', 'total_seconds': 320}
        ],
    'operating_systems':
        [
            {'digital': '0:05:20', 'hours': 0, 'minutes': 5, 'name': 'Windows', 'percent': 100.0, 'seconds': 20, 'text': '5 mins', 'total_seconds': 320}
        ],
    'projects':
        [
        {'branches': [
        {'digital': '0:05:20', 'hours': 0, 'minutes': 5, 'name': 'Unknown', 'percent': 100.0, 'seconds': 20, 'text': '5 mins', 'total_seconds': 320}
    ],
        'categories':
            [
            {'digital': '0:05:20', 'hours': 0, 'minutes': 5, 'name': 'Coding', 'percent': 100.0, 'seconds': 20, 'text': '5 mins', 'total_seconds': 320}
        ],
        'dependencies':
            [
            {'digital': '0:05:15', 'hours': 0, 'minutes': 5, 'name': 'discord', 'percent': 33.51, 'seconds': 15, 'text': '5 mins', 'total_seconds': 315},
            {'digital': '0:05:12', 'hours': 0, 'minutes': 5, 'name': 'Bot', 'percent': 33.19, 'seconds': 12, 'text': '5 mins', 'total_seconds': 312},
            {'digital': '0:05:08', 'hours': 0, 'minutes': 5, 'name': 'time', 'percent': 32.77, 'seconds': 8, 'text': '5 mins', 'total_seconds': 308},
            {'digital': '0:00:05', 'hours': 0, 'minutes': 0, 'name': 'json', 'percent': 0.53, 'seconds': 5, 'text': '5 secs', 'total_seconds': 5},
            {'digital': '0:00:00', 'hours': 0, 'minutes': 0, 'name': 'requests', 'percent': 0.0, 'seconds': 0, 'text': '0 secs', 'total_seconds': 0}
        ],
        'editors':
            [
            {'digital': '0:05:20', 'hours': 0, 'minutes': 5, 'name': 'PyCharmCore', 'percent': 100.0, 'seconds': 20, 'text': '5 mins', 'total_seconds': 320}
                       ],
        'entities': [
            {'digital': '0:05:08', 'hours': 0, 'minutes': 5, 'name': 'C:/Users/k260g/Desktop/untitled/main.py', 'percent': 96.25, 'seconds': 8, 'text': '5 mins', 'total_seconds': 308, 'type': 'file'},
            {'digital': '0:00:04', 'hours': 0, 'minutes': 0, 'name': 'C:/Users/k260g/Desktop/untitled/cogs/test.py', 'percent': 1.25, 'seconds': 4, 'text': '4 secs', 'total_seconds': 4, 'type': 'file'},
            {'digital': '0:00:03', 'hours': 0, 'minutes': 0, 'name': 'C:/Users/k260g/Desktop/untitled/Bot/KDE/decorators.py', 'percent': 0.94, 'seconds': 3, 'text': '3 secs', 'total_seconds': 3, 'type': 'file'},
            {'digital': '0:00:03', 'hours': 0, 'minutes': 0, 'name': 'C:/Users/k260g/Desktop/untitled/Bot/KDE/json_commands_changelog.py', 'percent': 0.94, 'seconds': 3, 'text': '3 secs', 'total_seconds': 3, 'type': 'file'},
            {'digital': '0:00:02', 'hours': 0, 'minutes': 0, 'name': 'C:/Users/k260g/Desktop/untitled/Bot/KDE/json_commands.py', 'percent': 0.62, 'seconds': 2, 'text': '2 secs', 'total_seconds': 2, 'type': 'file'},
            {'digital': '0:00:00', 'hours': 0, 'minutes': 0, 'name': 'C:/Users/k260g/Desktop/untitled/Bot/KDE/steam_request.py', 'percent': 0.0, 'seconds': 0, 'text': '0 secs', 'total_seconds': 0, 'type': 'file'}
        ],
        'grand_total': {'digital': '0:05', 'hours': 0, 'minutes': 5, 'percent': 100.0, 'text': '5 mins', 'total_seconds': 320},
        'languages': [
            {'digital': '0:05:20', 'hours': 0, 'minutes': 5, 'name': 'Python', 'percent': 100.0, 'seconds': 20, 'text': '5 mins', 'total_seconds': 320}
        ],
        'name': 'untitled',

        'operating_systems':
            [
            {'digital': '0:05:20', 'hours': 0, 'minutes': 5, 'name': 'Windows', 'percent': 100.0, 'seconds': 20, 'text': '5 mins', 'total_seconds': 320}
        ]
    }
    ]
}