from wakapy import User


a = User()
print(a.raw_day_containers)
pie_chart = a.pie_chart('lan')
pie_chart.show()
