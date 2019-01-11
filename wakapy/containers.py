class Parent:
    def __init__(self, _dict):
        self.digital = _dict.get('digital')
        self.hours = _dict.get('hours')
        self.minutes = _dict.get('minutes')
        self.name = _dict.get('name')
        self.percent = _dict.get('percent')
        self.seconds = _dict.get('seconds')
        self.text = _dict.get('text')
        self.time = _dict.get('total_seconds')
        self.type = _dict.get('type')

    def __repr__(self):
        return f"class <'{self.__class__.__name__}({self.name})'>"


class Project(Parent):
    def __init__(self, _dict):
        super().__init__(_dict=_dict)


class Os(Parent):
    def __init__(self, _dict):
        super().__init__(_dict=_dict)


class Language(Parent):
    def __init__(self, _dict):
        super().__init__(_dict=_dict)


class Entity(Parent):
    def __init__(self, _dict):
        super().__init__(_dict=_dict)


class Dependency(Parent):
    def __init__(self, _dict):
        super().__init__(_dict=_dict)


class Category(Parent):
    def __init__(self, _dict):
        super().__init__(_dict=_dict)


class Editor(Parent):
    def __init__(self, _dict):
        super().__init__(_dict=_dict)
