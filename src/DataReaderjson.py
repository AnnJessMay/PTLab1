from Types import DataType
from DataReader import DataReader
import json


class DataReaderJSON(DataReader):

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            data = json.load(file)
            for fio in data:
                temp_list = []
                for subject in data[fio]:
                    temp_list.append((subject, data[fio][subject]))
                self.students[fio] = temp_list
            return self.students
