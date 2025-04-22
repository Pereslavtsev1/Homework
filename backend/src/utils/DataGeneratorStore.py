from typing import List, Optional

from src.utils.DataGenerator import DataGenerator, DataGeneratorFactory
from src.utils.DataType import DataType


class DataGeneratorStore:
    def __init__(self) -> None:
        self.data_generators: List[DataGenerator] = [
            DataGeneratorFactory.createDataGenerator(data_type)
            for data_type in DataType
            if DataGeneratorFactory.createDataGenerator(data_type)
        ]

    def get_data_generator(self, type: DataType) -> Optional[DataGenerator]:
        for i in self.data_generators:
            if i.data_type == type:
                return i
        return None
