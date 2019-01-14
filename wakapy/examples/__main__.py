from wakapy import User

a = User('/home/surister/wakapy/wakapy/data/info.json')

a.get_days_between('2018-09-10', '2018-09-24')
chart = a.pie_chart('cat', use_slice=True)
chart.show()
