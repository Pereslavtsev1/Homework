import random
from enum import Enum


class Gender(Enum):
    FEMALE = "female"
    MALE = "male"


class Name:
    def __init__(self, name: str, gender: Gender):
        self.name = name
        self.gender = gender
    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, type(self)):
            return self.name == obj.name and self.gender == obj.gender
        return False
            

class FunRandomName:
    __names: list
    __adjectives: list

    def __init__(self):
        self.__names = []
        self.__adjectives = []

    def add_names(self, *args: Name) -> None:
        for i in args:
            if self.__isUnique(self.__names, i):
                self.__names.append(i)

    def get_name(self) -> str:
        name = self.__get_random_name()
        return self.__get_random_adjective(name) + " " + name.name

    def __get_random_adjective(self, name: Name) -> str:
        if len(self.__adjectives) == 0:
            raise RuntimeError(
                "The list of adjectives is empty. Please add adjectives before generating a name.")
        adjectives: str = self.__get_random_element_from_array(
            self.__adjectives)
        if name.gender == Gender.FEMALE:
            adjectives = adjectives[:-2] + "ая"
        return adjectives

    def __get_random_name(self) -> Name:
        if len(self.__names) == 0:
            raise RuntimeError(
                "The list of names is empty. Please add names before generating a name.")
        return self.__get_random_element_from_array(self.__names)

    def add_adjectives(self, *args: str) -> None:
        for i in args:
            if self.__isUnique(self.__adjectives, i):
                self.__adjectives.append(i)

    def __get_random_element_from_array(self, array: list):
        return random.choice(array)

    def __isUnique(self, array: list, item: Name):
        for i in array:
            if item.__eq__(i):
                return False
        return True