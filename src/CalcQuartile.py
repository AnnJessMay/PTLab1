from CalcRating import CalcRating
from Types import DataType
import statistics


class CalcQuartile:
    def __init__(self, data: DataType):
        self.data = data
        self.debt_count = 0

    def calc(self):
        rating = CalcRating(self.data).calc()
        sorted_rating = sorted(rating.values(), reverse=True)
        quartile_rating = statistics.quantiles(sorted_rating)[2]
        quartile_rating2 = filter(lambda x: quartile_rating < x[1],
                                  rating.items())
        return list(quartile_rating2)
