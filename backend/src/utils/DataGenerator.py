from abc import abstractmethod
from faker import Faker
from src.utils.DataType import DataType

import random


class DataGenerator:
    def __init__(
        self,
        data_type: DataType,
    ):
        self.data_type = data_type
        self.fake_ru = Faker("ru_RU")
        self.fake_en = Faker("en_US")

    @abstractmethod
    def generate_data(self, valid: bool) -> str:
        pass


class EmailGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.EMAIL)

    def generate_data(self, valid: bool):
        return self.fake_ru.email() if valid else self.fake_ru.email().replace("@", "")


class PhoneGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.PHONE)

    def generate_data(self, valid: bool):
        return (
            self.fake_ru.numerify("+7 (###) #### ## ##")
            if valid
            else self.fake_ru.numerify("+7 (###) #### ## ##").replace("+7", "a")
        )


class AddressGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.ADDRESS)

    def generate_data(self, valid: bool):
        return (
            self.fake_ru.address()
            if valid
            else f"Inv@lid Addr#ss {random.randint(1000, 9999)}"
        )


class BirthdateGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.BIRTHDATE)

    def generate_data(self, valid: bool):
        return (
            str(self.fake_ru.date_of_birth().strftime("%d.%m.%Y"))
            if valid
            else str(self.fake_ru.date_of_birth())
        )


class PassportGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.PASSPORT)

    def generate_data(self, valid: bool):
        return (
            (lambda s: s[:4].replace(" ", "") + s[4:])(self.fake_ru.passport_number())
            if valid
            else f"{''.join(random.choice('123456789') for _ in range(4))} {''.join(random.choice('ABCDEF') for _ in range(6))}"
        )


class PostcodeGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.POSTCODE)

    def generate_data(self, valid: bool):
        return (
            self.fake_ru.postcode()
            if valid
            else f"{''.join(random.choice('ABCDEF') for _ in range(6))}"
        )


class CountryGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.COUNTRY)

    def generate_data(self, valid: bool):
        return self.fake_en.country() if valid else "Not a Country"


class SNILSGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.SNILS)

    def generate_data(self, valid: bool):
        snils = self.fake_ru.snils()
        return (
            f"{snils[:3]}-{snils[3:6]}-{snils[6:9]} {snils[9:]}"
            if valid
            else self.fake_ru.numerify(text="########")
        )


class INNGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.INN)

    def generate_data(self, valid: bool):
        return (
            self.fake_ru.businesses_inn()
            if valid
            else self.fake_ru.numerify(text="#######")
        )


class BankCardGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.BANK_CARD)

    def generate_data(self, valid: bool):
        credit_card = self.fake_ru.credit_card_number()
        formatted_credit_card = " ".join(
            credit_card[i : i + 4] for i in range(0, len(credit_card), 4)
        )
        return (
            formatted_credit_card
            if valid
            else "4" + "".join(random.choice("ABCDEF") for _ in range(15))
        )


# TODO: change format
class IBANGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.IBAN)

    def generate_data(self, valid: bool):
        return self.fake_ru.iban() if valid else "GBXX ABCD 1234 5678"


class PaymentAmountGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.PAYMENT_AMOUNT)

    def generate_data(self, valid: bool):
        return (
            "{:.2f}".format(self.fake_ru.pyfloat(positive=True, max_value=10000))
            if valid
            else "{:.2f}".format(self.fake_ru.pyfloat(positive=False, max_value=0))
        )


class VINGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.VIN)

    def generate_data(self, valid: bool):
        return (
            self.fake_ru.vin()
            if valid
            else "INVALID_V" + "".join(random.choice("O0") for _ in range(5))
        )


class OrderDateGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.ORDER_DATE)

    def generate_data(self, valid: bool):
        return (
            str(self.fake_ru.date_between(start_date="-1y", end_date="today"))
            if valid
            else f"{random.randint(10000, 11000)}-{random.randint(13, 15):02}-{random.randint(32, 35):02}"
        )


class TimeGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.TIME)

    def generate_data(self, valid: bool):
        return (
            self.fake_ru.time()
            if valid
            else f"{random.randint(24, 99):02}:{random.randint(60, 99):02}:{random.randint(60, 99):02}"
        )


class URLGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.URL)

    def generate_data(self, valid: bool):
        return self.fake_ru.url() if valid else "not.a.url"


# FIX: type
class VehicleNumberGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.VEHICLE_NUMBER)

    def generate_data(self, valid: bool):
        return (
            self.fake_ru.license_plate_car()
            if valid
            else "".join(random.choice("!@#$%^&*()") for _ in range(9))
        )


class PasswordGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.PASSWORD)

    def generate_data(self, valid: bool):
        return self.fake_ru.password() if valid else self.fake_ru.password()[5:]


class MACAddressGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.MAC_ADDRESS)

    def generate_data(self, valid: bool):
        return self.fake_ru.mac_address() if valid else self.fake_ru.mac_address()[5:]


# TODO: fake coordinate generation
class CoordinatesGenerator(DataGenerator):
    def __init__(self):
        super().__init__(DataType.COORDINATES)

    def generate_data(self, valid: bool):
        return (
            f"{self.fake_ru.latitude()}, {self.fake_ru.longitude()}"
            if valid
            else "InvalidCoordinates"
        )
