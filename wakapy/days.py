from wakapy.containers import Os, Language, ADependency, Category, Editor, Project


class Day:
    def __init__(self, _dict):

        self.date = _dict.get('date')
        self.operative_systems = [Os(i) for i in _dict.get('operating_systems')]
        self.languages = [Language(i) for i in _dict.get('languages')]
        self.entities = [Dependency(i) for i in _dict.get('dependencies')]
        self.editors = [Editor(i) for i in _dict.get('editors')]
        self.categories = [Category(i) for i in _dict.get('categories')]
        self.projects = [Project(i) for i in _dict.get('projects')]

    def __repr__(self):
        return f"<class '{self.__class__.__name__}({self.date})'>"
