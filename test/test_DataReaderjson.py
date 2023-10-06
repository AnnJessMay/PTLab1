import os
import pytest
from src.Types import DataType
from src.DataReaderjson import DataReaderJSON


class TestDataReaderXML:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        root_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = f'{root_dir}/test_data.json'

        data = {'Иванов Иван Иванович': [('математика', 67), 
                                  ('литература', 100), 
                                  ('программирование', 91)], 
                'Петров Петр Петрович': [('математика', 78), 
                                         ('химия', 87), 
                                         ('социология', 61)]}

        return file_path, data

    def test_read(self, file_and_data_content: tuple[str, DataType]) -> None:
        file_content = DataReaderJSON().read(file_and_data_content[0])
        assert file_content == file_and_data_content[1]