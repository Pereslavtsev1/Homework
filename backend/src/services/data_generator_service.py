from typing import List

from src.utils.DataGenerator import (
    AddressGenerator,
    BirthdateGenerator,
    DataGenerator,
    EmailGenerator,
    PassportGenerator,
    PostcodeGenerator,
    CountryGenerator,
    SNILSGenerator,
    INNGenerator,
    BankCardGenerator,
    IBANGenerator,
    PaymentAmountGenerator,
    VINGenerator,
    OrderDateGenerator,
    TimeGenerator,
    PhoneGenerator,
    URLGenerator,
    VehicleNumberGenerator,
    PasswordGenerator,
    MACAddressGenerator,
    CoordinatesGenerator
)
from src.utils.DataType import DataType


class DataGeneratorService:
    def __init__(self):
        self.generators: List[DataGenerator] = [
            EmailGenerator(),
            PhoneGenerator(),
            AddressGenerator(),
            BirthdateGenerator(),
            PassportGenerator(),
            PostcodeGenerator(),
            CountryGenerator(),
            SNILSGenerator(),
            INNGenerator(),
            BankCardGenerator(),
            IBANGenerator(),
            PaymentAmountGenerator(),
            VINGenerator(),
            OrderDateGenerator(),
            TimeGenerator(),
            URLGenerator(),
            VehicleNumberGenerator(),
            PasswordGenerator(),
            MACAddressGenerator(),
            CoordinatesGenerator()
        ]

    def generate_data(self, type: DataType, valid: bool):
        for i in self.generators:
            if i.data_type.__eq__(type):
                return i.generate_data(valid)
        return "Error"
# jjjj
