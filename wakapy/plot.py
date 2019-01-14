import matplotlib.pyplot as plt


def get_labels(l, hours, items):
    total_sum = sum(l)

    it = 0
    temp_list = []
    for p in l:
        pct = (p / total_sum) * 100
        temp_list.append(f'{items[it]} - {hours[it]} ({round(pct, 2)}%)')
        it += 1
    return temp_list


class PieChart:
    def __init__(self, _dict, num, dates=None):
        self.dict = _dict
        self.fig = None

        items = list(self.dict.keys())
        data = list(map(lambda x: x / 3600, self.dict.values()))

        item1 = items[:num]
        data1 = data[:num]

        hours = list(map(lambda x: f'{round(x, 2)}h', data1))
        labels = get_labels(data1, hours, item1)
        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(aspect='equal'))
        wedges, texts = ax.pie(data1)

        ax.legend(wedges, labels,
                  title=f"|{dates[0].date} | {dates[1].date}|",
                  loc=2,
                  bbox_to_anchor=(1, 0)
                  )

    def show(self) -> None:
        self.fig = plt.gcf()
        plt.show()

    def save(self, fp: str) -> None:
        fig = self.fig if self.fig else plt.gcf()
        fig.savefig(fp, bbox_inches='tight', format='png', dpi=100)

    def __repr__(self):
        return f"class <'{self.__class__.__name__}{self.dict}'>"
