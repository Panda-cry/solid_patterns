from abc import ABC, abstractmethod


class Implementation(ABC):

    @abstractmethod
    def operation_implementation(self):
        pass


class Abstraction:

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self):
        return self.implementation.operation_implementation()


class ExtendedAbstraction(Abstraction):

    def operation(self):
        return self.implementation.operation_implementation()


class ConcreteImplementation1(Implementation):

    def operation_implementation(self):
        return f"Concrete Implementation #1"


class ConcreteImplementation2(Implementation):

    def operation_implementation(self):
        return f"Concrete Implementation #2"


def client(abstraction: Abstraction):
    print(abstraction.operation())


if __name__ == "__main__":
    client(Abstraction(ConcreteImplementation1()))
    client(ExtendedAbstraction(ConcreteImplementation2()))


#Malo mi je ovo cudno
#imamo 2 implementacije
#gde kasnije kreiramo 2 Abstrakcije
#koje svakako pozivaju 1 metudu od Interfejsa Implementacije
#i kasnije samo koristimo apstrakcije i tjt
#mislim da sam ukapirao
#ako imamo nesto komplikovano
#ovde se trudi da podelimo na 2 hijarahije
#npr imamo uredjaje TV/RAdio/Klima
#i daljinac jedan
#verovatno da pracenje samo jednog uredjaja bi bilo konfuzno
#napravimo i daljinac klasu koja ima uredjaje i radi sa njima sta zna
#zato imamo kompoziciju tj klasu kao polje 2 klase
#Fazno mozemo da ubacimo fabriku da kreira neke proizvode jer imaju samo 1 interfejs
#kasnije pravimo apstrakcije necega gde koristimo implementacije


# OVako ja vidim to. Neka fabrika napravi neke instance prema nekim interfejsu. Recimo da imamo abstraktnu fabriku televizora, gde se vracaju neki TV, i da pravimo apstrakcije daljinskih upravljaca koji imaju jedno polje kao kompoziciju tv i kasnije samo pravimo razlicite daljince sa odredjenim metodama i tjt