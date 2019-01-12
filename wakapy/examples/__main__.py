from wakapy import User


a = User()
print(a.total_worked_days)
pie_chart = a.top_5_pie_chart('lan')
pie_chart.show()

