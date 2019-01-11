from wakapy import User


a = User()

pie_chart = a.top_5_pie_chart('lan')
pie_chart.show()
print(pie_chart)
print(a)