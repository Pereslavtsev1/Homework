from typing import Callable

from faker import Faker
import random
from src.utils.DataType import DataType

fake_ru = Faker("ru_RU")
fake_en = Faker("en_US")


class DataGenerator:
    def __init__(
        self,
        data_type: DataType,
        generate_data: Callable[[bool], str],
    ):
        self.data_type = data_type
        self.generate_data = generate_data


class DataGeneratorFactory:
    @staticmethod
    def createDataGenerator(type: DataType) -> DataGenerator:
        if type == DataType.EMAIL:
            return DataGenerator(
                DataType.EMAIL,
                lambda valid: fake_ru.email()
                if valid
                else fake_ru.email().replace("@", ""),
            )
        elif type == DataType.PHONE:
            return DataGenerator(
                DataType.PHONE,
                lambda valid: fake_ru.phone_number()
                if valid
                else fake_ru.phone_number()[:2],
            )
        elif type == DataType.ADDRESS:
            return DataGenerator(
                DataType.ADDRESS,
                lambda valid: fake_ru.address()
                if valid
                else f"Inv@lid Addr#ss {fake_ru.numerify('####')}",
            )
        elif type == DataType.BIRTHDATE:
            return DataGenerator(
                DataType.BIRTHDATE,
                lambda valid: str(fake_ru.date_of_birth().strftime("%d.%m.%Y"))
                if valid
                else str(fake_ru.date_of_birth()),
            )

        elif type == DataType.PASSPORT:
            return DataGenerator(
                DataType.PASSPORT,
                lambda valid: (lambda s: s[:4].replace(" ", "") + s[4:])(
                    fake_ru.passport_number()
                )
                if valid
                else fake_ru.numerify("########"),
            )
        elif type == DataType.POSTCODE:
            return DataGenerator(
                DataType.POSTCODE,
                lambda valid: fake_ru.postcode()
                if valid
                else f"{''.join(random.choice('ABCDEF') for _ in range(6))}",
            )
        elif type == DataType.COUNTRY:
            return DataGenerator(
                DataType.COUNTRY,
                lambda valid: fake_en.country() if valid else "Not a Country",
            )
        elif type == DataType.SNILS:
            snils = fake_ru.snils()
            return DataGenerator(
                DataType.SNILS,
                lambda valid: f"{snils[:3]}-{snils[3:6]}-{snils[6:9]} {snils[9:]}"
                if valid
                else fake_ru.numerify(text="########"),
            )
        elif type == DataType.INN:
            return DataGenerator(
                DataType.INN,
                lambda valid: fake_ru.businesses_inn()
                if valid
                else fake_ru.numerify(text="#######"),
            )
        elif type == DataType.BANK_CARD:
            credit_card = fake_ru.credit_card_number()
            formatted_credit_card = " ".join(
                credit_card[i : i + 4] for i in range(0, len(credit_card), 4)
            )
            return DataGenerator(
                DataType.BANK_CARD,
                lambda valid: formatted_credit_card
                if valid
                else "4" + "".join(random.choice("ABCDEF") for _ in range(15)),
            )

        # TODO: change format
        elif type == DataType.IBAN:
            return DataGenerator(
                DataType.IBAN,
                lambda valid: fake_ru.iban()
                if valid
                else fake_ru.numerify(text="##########"),
            )

        elif type == DataType.PAYMENT_AMOUNT:
            return DataGenerator(
                DataType.PAYMENT_AMOUNT,
                lambda valid: "{:.2f}".format(
                    fake_ru.pyfloat(positive=True, max_value=10000)
                )
                if valid
                else "{:.2f}".format(fake_ru.pyfloat(positive=False, max_value=0)),
            )
        elif type == DataType.VIN:
            return DataGenerator(
                DataType.VIN,
                lambda valid: fake_ru.vin()
                if valid
                else "INVALID_V" + "".join(random.choice("O0") for _ in range(5)),
            )
        elif type == DataType.ORDER_DATE:
            return DataGenerator(
                DataType.ORDER_DATE,
                lambda valid: str(
                    fake_ru.date_between(start_date="-1y", end_date="today")
                )
                if valid
                else f"{random.randint(10000, 11000)}-{random.randint(13, 15):02}-{random.randint(32, 35):02}",
            )
        elif type == DataType.TIME:
            return DataGenerator(
                DataType.TIME,
                lambda valid: fake_ru.time()
                if valid
                else f"{random.randint(24, 99):02}:{random.randint(60, 99):02}:{random.randint(60, 99):02}",
            )
        elif type == DataType.URL:
            return DataGenerator(
                DataType.URL, lambda valid: fake_ru.url() if valid else "not.a.url"
            )

        #  FIX: incorect type format
        elif type == DataType.VEHICLE_NUMBER:
            return DataGenerator(
                DataType.TIME,
                lambda valid: fake_ru.license_plate_car()
                if valid
                else "".join(random.choice("!@#$%^&*()") for _ in range(9)),
            )
        elif type == DataType.PASSWORD:
            return DataGenerator(
                DataType.PASSWORD,
                lambda valid: fake_ru.password() if valid else fake_ru.password()[5:],
            )
        elif type == DataType.MAC_ADDRESS:
            return DataGenerator(
                DataType.MAC_ADDRESS,
                lambda valid: fake_ru.mac_address()
                if valid
                else fake_ru.mac_address()[5:],
            )

        #  TODO: fake coordinate genertion
        elif type == DataType.COORDINATES:
            return DataGenerator(
                DataType.COORDINATES,
                lambda valid: f"{fake_ru.latitude()}, {fake_ru.longitude()}"
                if valid
                else "InvalidCoordinates",
            )
