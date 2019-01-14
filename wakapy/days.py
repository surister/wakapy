from wakapy.containers import Os, Language, Dependency, Category, Editor, Project


class Day:
    def __init__(self, _dict):

        self.date = _dict.get('date')
        self.operative_systems = [Os(i) for i in _dict.get('operating_systems')]
        self.languages = [Language(i) for i in _dict.get('languages')]
        self.entities = [Dependency(i) for i in _dict.get('dependencies')]
        self.editors = [Editor(i) for i in _dict.get('editors')]
        self.categories = [Category(i) for i in _dict.get('categories')]
        self.projects = [Project(i) for i in _dict.get('projects')]

        self.year, self.month, self.day = self.date.split('-')

        self.is_empty = bool(not self.operative_systems)

        self.container_dict = {'os': self.operative_systems,
                               'lan': self.languages,
                               'ent': self.entities,
                               'edit': self.editors,
                               'cat': self.categories,
                               'proj': self.projects
                               }

    def split(self, splitwith: str) -> str:
        return self.date.split(splitwith)

    def __repr__(self):
        return f"<class '{self.__class__.__name__}({self.date})'>"
