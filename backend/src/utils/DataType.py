from enum import Enum


class DataType(str, Enum):
    EMAIL = "email"
    PHONE = "phone"
    ADDRESS = "address"
    BIRTHDATE = "birthdate"
    PASSPORT = "passport"
    POSTCODE = "postcode"
    COUNTRY = "country"
    SNILS = "snils"
    INN = "inn"
    BANK_CARD = "bank_card"
    IBAN = "iban"
    PAYMENT_AMOUNT = "payment_amount"
    VIN = "vin"
    ORDER_DATE = "order_date"
    TIME = "time"
    URL = "url"
    VEHICLE_NUMBER = "vehicle_number"
    PASSWORD = "password"
    MAC_ADDRESS = "mac_address"
    COORDINATES = "coordinates"
