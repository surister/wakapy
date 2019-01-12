from wakapy import User


a = User()
print(a.total_worked_days)
pie_chart = a.pie_chart('edit', num=4)
pie_chart.show()

