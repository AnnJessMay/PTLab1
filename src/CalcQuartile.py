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
        median_q_2 = statistics.median([x[1] for x in sorted_rating])
        q_2 = list(filter(lambda x: median_q_2 < x[1], sorted_rating))
        median_q_3 = statistics.median(x[1] for x in q_2)
        q_3 = filter(lambda x: median_q_3 < x[1], q_2)
        return dict(q_3)


if __name__ == "__main__":
    data = DataReaderJSON().read('../data/data.json')
