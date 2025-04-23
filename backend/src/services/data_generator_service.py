from src.utils.DataGeneratorStore import DataGeneratorStore
from src.utils.DataType import DataType


class DataGeneratorService:
    @staticmethod
    def generate_data(type: DataType, valid: bool):
        generator = DataGeneratorStore().get_data_generator(type)
        if generator:
            return generator.generate_data(valid)
        else:
            raise ValueError(f"No data generator found for type: {type}")
