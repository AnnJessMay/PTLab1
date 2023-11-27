from CalcRating import CalcRating
from DataReaderJSON import DataReaderJSON
from Types import DataType
import statistics


class CalcQuartile:
    def __init__(self, data: DataType):
        self.data = data
        self.debt_count = 0

    def calc(self):
        rating = CalcRating(self.data).calc()
        sorted_rating = sorted(rating.items(), key=lambda x: x[1],
                               reverse=True)
        quartile_rating = statistics.quantiles(sorted_rating.values())
        quartile_rating2 = filter(lambda x: quartile_rating < x[1], sorted_rating)
        return dict(quartile_rating2)


if __name__ == "__main__":
    data = DataReaderJSON().read('../data/data.json')
