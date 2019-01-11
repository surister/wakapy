

class Parent:
    def __init__(self, _dict):
        self.digital = _dict.get('digital')
        self.hours = _dict.get('hours')
        self.minutes = _dict.get('minutes')
        self.name = _dict.get('name')
        self.percent = _dict.get('percent')
        self.seconds = _dict.get('seconds')
        self.text = _dict.get('text')
        self.total_time = _dict.get('total_seconds')
        self.type = _dict.get('type')

    def __repr__(self):
        return f"class <'{self.__class__.__name__}({self.name})'>"


class Project:
    untitled_counter = 0

    def __init__(self, _dict):
        self.name = _dict.get('name')

        self.is_untitled = False
        if self.name == 'untitled':
            Project.untitled_counter += 1
            self.is_untitled = True
        self.num = Project.untitled_counter

        self.branches = [Branch(i) for i in _dict.get('branches')]
        self.categories = [Category(i) for i in _dict.get('categories')]
        self.dependencies = [Dependency(i) for i in _dict.get('dependencies')]
        self.editors = [Editor(i) for i in _dict.get('editors')]
        self.entities = [Entity(i) for i in _dict.get('entities')]
        self.languages = [Language(i) for i in _dict.get('languages')]
        self.operative_systems = [Os(i) for i in _dict.get('operating_systems')]

        self.repr_string = f'-{self.num}' if self.is_untitled else ""

    def __repr__(self):
        return f"class <'{self.__class__.__name__}({self.name}{self.repr_string})'>"


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


class Branch(Parent):
    def __init__(self, _dict):
        super().__init__(_dict=_dict)
