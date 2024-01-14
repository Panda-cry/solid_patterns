from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def operation(self):
        pass


class Creator(ABC):
    """
    Crator klasa ima metodu koja treba da vrati konkretnu klasu
    """

    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self):
        product = self.factory_method()

        return product.operation()


class ConcreteProduct1(Product):

    def operation(self):
        return "Product 1"


class ConcreteProduct2(Product):

    def operation(self):
        return "Product 2"


class ConcreteCreator1(Creator):

    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self):
        return ConcreteCreator2()


def client_code(creator: Creator) -> None:
    print(creator.some_operation())


if __name__ == "__main__":
    client_code(ConcreteCreator1())

#Factory neka primena je da se vracaju instance
#ali da klasa naslednica moze da izmeni klasu
#tj moze da vrati bilo sta kao sto ovde imamo Product1 i Produtc2
#kreira se samo jedan proizvod dok kod abstract se kreira familija prozivoda
