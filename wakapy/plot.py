import matplotlib.pyplot as plt


class PieChart:
    def __init__(self, _dict, num=None):
        self.dict = _dict

        items = list(self.dict.keys())
        data = list(map(lambda x: x / 3600, self.dict.values()))

        if num:
            item1 = items[:]
            data1 = data[:num]

        else:
            data1 = data
            item1 = items

        print(data)
        labels_raw = list(map(lambda x: f'{round(x, 2)}h', data1))

        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(aspect='equal'))
        wedges, texts = ax.pie(data1)

        ax.legend(wedges, item1,
                  title=f"Top {num}",
                  loc=2,
                  bbox_to_anchor=(1, 0)
                  )

        #plt.savefig('/home/surister/wakapy/wakapy/data/as.png')

    @staticmethod
    def show():
        plt.show()

    @staticmethod
    def save(fp):
        plt.savefig(fp)

    def __repr__(self):
        return f"class <'{self.__class__.__name__}{self.dict}'>"
