from wakapy.parser import JsonFile
from wakapy.exceptions import EmptyFolderError, ContainerNotFound
from wakapy.utils import order_dict, Constants
from wakapy.plot import PieChart


class User:
    def __init__(self, fp=None, file_number=0):

        files = Constants.data_files
        if not files and fp is None:
            raise EmptyFolderError('Io folder is empty and no file path was given')

        self.fp = files[file_number] if fp is None else fp

        self.file = JsonFile(self.fp)
        user_info = self.file.user_info

        self.display_name = user_info.get('display_name')
        self.created_at = user_info.get('created_at')
        self.email = user_info.get('email')
        self.is_email_public = user_info.get('is_email_public')
        self.full_name = user_info.get('full_name')
        self.has_premium_features = user_info.get('has_premium_features')
        self.human_readable_website = user_info.get('human_readable_website')
        self.id = user_info.get('id')
        self.is_email_confirmed = user_info.get('is_email_confirmed')
        self.is_hireable = user_info.get('is_hireable')
        self.languages_used_public = user_info.get('languages_used_public')
        self.last_heartbeat = user_info.get('last_heartbeat')
        self.last_plugin = user_info.get('last_plugin')
        self.last_plugin_name = user_info.get('last_plugin_name')
        self.last_project = user_info.get('last_project')
        self.location = user_info.get('location')
        self.logged_time_public = user_info.get('logged_time_public')
        self.modified_at = user_info.get('modified_at')
        self.photo = user_info.get('photo')
        self.photo_public = user_info.get('photo_public')
        self.plan = user_info.get('plan')
        self.timeout = user_info.get('timeout')
        self.timezone = user_info.get('timezone')
        self.username = user_info.get('username')
        self.website = user_info.get('website')
        self.writes_only = user_info.get('writes_only')

        self.raw_day_containers = self.days[0].container_dict  # Just the first one makes it.

    @property
    def days(self):
        return self.file.days

    @property
    def total_worked_days(self):
        total = 0
        for day in self.days:
            if not day.is_empty:
                total += 1
        return total

    def _fetch_data(self, to_fetch: str) -> dict:
        if to_fetch not in self.raw_day_containers:
            raise ContainerNotFound(f"<'Day'> class has no {to_fetch} container - attribute")

        temp_dic = {}
        for day in self.days:
            if not day.is_empty:
                for container in day.container_dict[to_fetch]:
                    if container.name not in temp_dic.keys():
                        temp_dic[container.name] = container.total_time
                    else:
                        temp_dic[container.name] += container.total_time

        return order_dict(temp_dic, True)

    def pie_chart(self, to_fetch: str, num: int =10) -> PieChart:
        return PieChart(self._fetch_data(to_fetch), num=num)

    def __repr__(self):
        return f'class <{self.__class__.__name__}({self.username})>'

    def __len__(self):
        return len(self.days)
