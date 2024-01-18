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



#Recimo da imamo neki Podatak sto je abstraktna klasa i mora imati metodu serialize
#Mozemo da kreiramo PodtakJson koji implementira tu vrstu serializaciju PodatakXml, PodatakHtml
#oni implementiraju tu serializaciju na svoj nacin
# Onda kreiramo fabriku koja poziva tu metodu i vraca nam serializovani objekat
# Factory bi trebao da vraca instance tih CreatorKlasa Znaci PodatakJsonCreaator sa metodom

#obicno se koriste za neke library da mogu naredni developeri da nadograde svoje custom zahteve
#tokom testiranja za mock nekih podatak



#Razlika izmedju factory i abstract factory je da se ovde radi o samo jedno podatku
#dok tamo imamo vise podataka koji trebaju da budu na neki nacin razliciti
#NPR WIndows familija i Linux familija gde su podaci Dugme/Prozor/Kursor/Teme itd.