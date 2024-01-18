# problematika je da bude nesto jedinstveno
# da nakalemimo nesto novo na base klasu
# koristiti builder kada zelimo da kod kreira
# dosta razlicitih reprezentacija nekog proizvoda
from abc import ABC, abstractmethod
from typing import Any


class Product1:

    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        print(part)
        self.parts.append(part)

    def list_parts(self):
        print(self.parts)


class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass


class ConcreteBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        print("aha")
        self._product.add("Part A")

    def produce_part_b(self):
        self._product.add("Part B")


class Director:

    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def build_minimal_product(self):
        self._builder.produce_part_a()

    def build_full_product(self):
        self._builder.produce_part_a()
        self._builder.produce_part_b()


if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder

    director.build_minimal_product()
    print(director.builder.product().list_parts())

    director.build_full_product()
    print(director.builder.product().list_parts())


#sve u svemu trebamo da imamo proizvod neki
#nakon toga neke metode koje treba da nam rese buildovanje
#Builder treba da poziva te metode i da napravi jedinstven objekat
# NPR Proizvod je auto koji ima metode vrata (5,3) set felni(18/19/17 inch)
#zatamnjena stakla, body kit itd to su seteri i geteri
# onda mozemo da imamo 2/3 buildera koja kreiraju ModeranAuto,SportskiAuto, Klasik, Custom itd
# kasnije ih samo kreiramo i vracamo sta se zahtevalo :D


#Jedan zajednicki prozivod koji treba da se modifikuje sa builderima
# Jedan bulderi sa fjoma koji menjaju proizvod
# Vise direktora koji pozivaju fje i menjaju
#Koliko sam ukapirao builder treba da ima metode koje su get/set za objekat i tjt
# pozivima buildera kreiramo sta nam treba
