import datetime

from wakapy.parser import JsonDict
from wakapy.exceptions import ContainerNotFound
from wakapy.utils import order_dict
from wakapy.plot import PieChart


class Slice:
    def __init__(self, days, date_1=None, date_2=None):

        if not isinstance(date_1, str) and not isinstance(date_1, str) \
                and not isinstance(date_1, datetime.date) and not isinstance(date_2, datetime.date):
            raise TypeError("Parameters given have to be either <'str'> or <'datetime.date> objects")

        for date in (date_1, date_2):  # dateutils could be used instead of this.
            if not isinstance(date, datetime.date):
                try:
                    datetime.datetime.strptime(date, '%Y-%m-%d')
                except ValueError:
                    raise ValueError(f"Incorrect data format, should be YYYY-MM-DD, not {date}")

        self.date1 = date_1
        self.date2 = date_2

        index = 0
        for _date in (self.date1, self.date2):

            if isinstance(_date, str) and index == 0:
                year, month, day = _date.split('-')
                self.date1 = datetime.date(year=int(year), month=int(month), day=int(day))

            if isinstance(_date, str) and index == 1:
                year, month, day = _date.split('-')
                self.date2 = datetime.date(year=int(year), month=int(month), day=int(day))

            index += 1

        if self.date1 > self.date2:
            raise ValueError('date 2 cannot be bigger than date 1')

        self.raw_days = days

    def _get_sliced_days(self):
        index1 = None
        index2 = None
        for index, day in enumerate(self.raw_days):

            if int(day.year) == self.date1.year:
                if int(day.month) == self.date1.month:
                    if int(day.day) == self.date1.day:
                        index1 = index

            if int(day.year) == self.date2.year:
                if int(day.month) == self.date2.month:
                    if int(day.day) == self.date2.day:
                        index2 = index

        if None in (index1, index2):
            raise ValueError('One of your dates do not exist')
        return self.raw_days[index1: index2 + 1]

    @property
    def days(self):
        return self._get_sliced_days()

    def __repr__(self):
        return f'class <{self.__class__.__name__}>'


class User:
    def __init__(self, fp: str):

        self.fp = fp
        self.file = JsonDict(self.fp)
        user_info = self.file.user_data

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

        self.slice = None
        self._raw_day_containers = self.days[0].container_dict  # Just the first one makes it.

    @property
    def days(self):
        return self.file.days

    @property
    def total_worked_days(self) -> int:
        total = 0
        for day in self.days:
            if not day.is_empty:
                total += 1
        return total

    def _fetch_data(self, to_fetch: str, use_slice: bool) -> dict:

        if to_fetch not in self._raw_day_containers:
            raise ContainerNotFound(f"<'Day'> class has no {to_fetch} container - attribute")

        if use_slice and self.slice:
            data = self.slice
        elif use_slice and not self.slice:
            raise ValueError('There is no slice created')
        else:

            data = self.days

        temp_dic = {}
        for day in data:

            if not day.is_empty:
                for container in day.container_dict[to_fetch]:
                    if container.name not in temp_dic.keys():
                        temp_dic[container.name] = container.total_time
                    else:
                        temp_dic[container.name] += container.total_time

        return order_dict(temp_dic, True)

    def get_days_between(self, date1=None, date2=None) -> list:
        self.slice = Slice(self.days, date_1=date1, date_2=date2).days
        return self.slice

    def pie_chart(self, to_fetch: str, num: int =10, use_slice=False) -> PieChart:
        return PieChart(self._fetch_data(to_fetch, use_slice), num=num, dates=(self.slice[0], self.slice[::-1][0]))

    def __repr__(self):
        return f'class <{self.__class__.__name__}({self.username})>'

    def __len__(self):
        return len(self.days)
