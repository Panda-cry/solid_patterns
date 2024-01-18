from abc import ABC, abstractmethod
from enum import Enum


class CarBodyKit(Enum):
    SPORT = "sport"
    CLASSIC = "classic"
    ELEGANT = "elegant"
    COMFORT = "comfort"


class Car:

    def __init__(self):
        self.doors = 5
        self.color = "red"
        self.b_kit = CarBodyKit.CLASSIC

    @property
    def door(self):
        return self.doors

    @door.setter
    def door(self, doors):
        self.doors = doors

    @property
    def col(self):
        return self.color

    @col.setter
    def col(self, color):
        self.color = color

    @property
    def kit(self):
        return self.b_kit

    @kit.setter
    def kit(self, kit):
        self.b_kit = kit

    def __str__(self):
        return f"Car have {self.doors} doors, \n body kit {self.kit.value} and paint is {self.color}\n"


class Builder(ABC):

    def __init__(self):
        self.car = Car()

    @abstractmethod
    def set_body_kit(self):
        pass

    @abstractmethod
    def set_doors(self):
        pass

    @abstractmethod
    def set_color(self):
        pass


class CarBuilder(Builder):

    def set_body_kit(self, kit):
        self.car.kit = kit

    def set_color(self, color):
        self.car.color = color

    def set_doors(self, doors):
        self.car.door = doors



class SportDirector:

    def __init__(self):
        self._builder = CarBuilder()

    def create_car(self) -> Car:
        self._builder.set_color("yellow")
        self._builder.set_body_kit(CarBodyKit.SPORT)
        self._builder.set_doors(3)

        return self._builder.car


class ModernDirector:

    def __init__(self):
        self._builder = CarBuilder()

    def create_car(self) -> Car:
        self._builder.set_color("green")
        self._builder.set_body_kit(CarBodyKit.COMFORT)
        self._builder.set_doors(5)

        return self._builder.car


class Fabric(ABC):

    @abstractmethod
    def fabric_method(self):
        pass

    


class ModernCarFabric(Fabric):

    def __init__(self):
        self.director = ModernDirector()

    def fabric_method(self) -> Car:
        return self.director.create_car()


class SportCarFabric(Fabric):

    def __init__(self):
        self.director = SportDirector()

    def fabric_method(self) -> Car:
        return self.director.create_car()


def create_car(fabric: Fabric):
    print(fabric.fabric_method())


if __name__ == "__main__":
    car = create_car(SportCarFabric())
