# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcQuartile import CalcQuartile
import pytest

RatingsType = dict[str, float]


class TestCalcQuartile:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61)
            ],
            "Сидоров Сергей Иванович": [
                ("математика", 80),
                ("биология", 100),
                ("физика", 91)
            ],
            "Фролов Лев Алексеевич": [
                ("физика", 80),
                ("химия", 98),
                ("литература", 96)
            ]
        }

        rating_scores = [('Фролов Лев Алексеевич', 91.33333333333333)]
        return data, rating_scores

    def test_init_calc_rating(self, input_data: tuple[DataType, RatingsType]):
        calc_quartile = CalcQuartile(input_data[0])
        assert input_data[0] == calc_quartile.data

    def test_calc(self, input_data: tuple[DataType, RatingsType]):
        rating = CalcQuartile(input_data[0]).calc()
        for student_rating in rating:
            assert student_rating[0] == input_data[1][0][0]
            assert student_rating[1] == input_data[1][0][1]
