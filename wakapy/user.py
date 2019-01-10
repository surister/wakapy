from pathlib import PurePath, Path

from wakapy.parser import Injector
from wakapy.exceptions import EmptyFolderError

io_path = PurePath(PurePath(__file__).parent).joinpath('io/')
files = [file for file in Path(io_path).iterdir()]


class User:
    def __init__(self, fp=None, file_number=0):

        if not files and fp is None:
            raise EmptyFolderError('Io folder is empty and no file path was given')

        self.fp = files[file_number] if fp is None else fp
        kw = Injector().info(self.fp)

        self.display_name = kw.get('display_name')
        self.created_at = kw.get('created_at')
        self.email = kw.get('email')
        self.is_email_public = kw.get('is_email_public')
        self.full_name = kw.get('full_name')
        self.has_premium_features = kw.get('has_premium_features')
        self.human_readable_website = kw.get('human_readable_website')
        self.id = kw.get('id')
        self.is_email_confirmed = kw.get('is_email_confirmed')
        self.is_hireable = kw.get('is_hireable')
        self.languages_used_public = kw.get('languages_used_public')
        self.last_heartbeat = kw.get('last_heartbeat')
        self.last_plugin = kw.get('last_plugin')
        self.last_plugin_name = kw.get('last_plugin_name')
        self.last_project = kw.get('last_project')
        self.location = kw.get('location')
        self.logged_time_public = kw.get('logged_time_public')
        self.modified_at = kw.get('modified_at')
        self.photo = kw.get('photo')
        self.photo_public = kw.get('photo_public')
        self.plan = kw.get('plan')
        self.timeout = kw.get('timeout')
        self.timezone = kw.get('timezone')
        self.username = kw.get('username')
        self.website = kw.get('website')
        self.writes_only = kw.get('writes_only')

    def __repr__(self):
        return f'class <{self.__class__.__name__}({self.username})>'
