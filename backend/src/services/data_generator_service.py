from src.utils.DataGeneratorStore import DataGeneratorStore
from src.utils.DataType import DataType


class DataGeneratorService:
    def __init__(self):
        self.store = DataGeneratorStore()

    def generate_data(self, type: DataType, valid: bool):
        generator = self.store.get_data_generator(type)
        if generator:
            return generator.generate_data(valid)
        else:
            raise ValueError(f"No data generator found for type: {type}")
