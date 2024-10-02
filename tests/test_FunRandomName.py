
import pytest

from src.RandomName import FunRandomName, Gender, Name


class TestFunRandomName:
    @pytest.fixture
    def fun_random_name(self) -> FunRandomName:
        return FunRandomName()

    def test_add_random_method_without_duplicate(self, fun_random_name):
        name1: Name = Name("Кот", Gender.MALE)
        name2: Name = Name("Кошка", Gender.FEMALE)
        fun_random_name.add_names(name1,name2)
        names_size = getattr(fun_random_name, '_FunRandomName__names')
        assert len(names_size) == 2
    def test_add_random_method_with_duplicate(self,fun_random_name):
        name1 = Name("Кот",Gender.MALE)
        name2 = Name("Кот",Gender.MALE)
        fun_random_name.add_names(name1,name2)
        names_size = getattr(fun_random_name, '_FunRandomName__names')
        print(names_size)
        assert len(names_size) == 1
    def test_get_name_without_adjectives_raises_exception(self, fun_random_name):
        name1 = Name("Кошка", Gender.FEMALE)
        fun_random_name.add_names(name1)
        with pytest.raises(RuntimeError):
            fun_random_name.get_name()
    def test_get_name_without_names_raises_exception(self, fun_random_name):
        with pytest.raises(RuntimeError):
            fun_random_name.get_name()
    def test_get_name_for_female(self,fun_random_name: FunRandomName):
        name1= Name("Кошка",Gender.FEMALE)
        fun_random_name.add_adjectives("Красивый")
        fun_random_name.add_names(name1)
        assert fun_random_name.get_name() == "Красивая Кошка"