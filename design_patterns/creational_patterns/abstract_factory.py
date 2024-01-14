from abc import ABC, abstractmethod


class AbstractProductA(ABC):

    @abstractmethod
    def method_a(self):
        pass


class AbstractProductB(ABC):

    @abstractmethod
    def method_b(self):
        pass


class AbstractFactory(ABC):

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteProductA1(AbstractProductA):

    def method_a(self):
        print("This is product A1")


class ConcreteProductA2(AbstractProductA):

    def method_a(self):
        print("This is product A2")


class ConcreteProductB1(AbstractProductB):

    def method_b(self):
        print("This is product B1")


class ConcreteProductB2(AbstractProductB):

    def method_b(self):
        print("This is product B2")


class ConcreteFabric1(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFabric2(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


def client_code(factory : AbstractFactory):

    product_a = factory.create_product_a()
    product_b = factory.create_product_b()


    product_a.method_a()
    product_b.method_b()


if __name__ == "__main__":

    factory1 = ConcreteFabric1()
    factory2 = ConcreteFabric2()

    client_code(factory1)
    client_code(factory2)


#Osnova je da se naprave neke familije slicnih proizvoda
#ali da znamo samo fabriku ne i konkretne modele
#primena je kada ne zelimo da menjamo kod
#nego zelimo da promenimo porodicu
#tipa imamo vozila neka Ford, Skoda
#zelimo da omogucimo nesto znaci da dodamo Mercedes i nesto njegovo


#npr familija objekata
# prevoz tipa
# Interfejs transoport + motor + upravljanje
# mozemi imati auto + dize + volan
# avion + mlaznjak + dzojstik :D