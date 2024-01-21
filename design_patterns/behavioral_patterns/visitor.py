from abc import ABC, abstractmethod
from typing import List


class Visitor(ABC):

    @abstractmethod
    def visit_concrete_component_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element):
        pass


class Component(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class ConcreteComponentA(Component):

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_a(self)

    def self_function_a(self):
        return "a"


class ConcreteComponentB(Component):

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_b(self)

    def self_function_b(self):
        return "b"


class ConcreteVisitor(Visitor):

    def visit_concrete_component_a(self, element):
        print(f"{element.self_function_a()} + Visitor :D")

    def visit_concrete_component_b(self, element):
        print(f"{element.self_function_b()} + Visitor :D ")


def client_code(components: List[Component], visitor: Visitor):

    for component in components:
        component.accept(visitor)



if __name__ == "__main__":

    components = [ConcreteComponentA(), ConcreteComponentB()]

    visitor = ConcreteVisitor()

    client_code(components, visitor)


#visitor kao i sama rec posecuje druge klase
# da bi napravio neku novu funkcionalnost ne mora da se dodaje nista u te druge klase
# sto je i dobro sta ako zelimo jos nesto da dodamo pored te novine
# bolje da kreiramo i vise visitora nego da menjamo klasu tako da bude glomazna
# Double Dispath !!! imamo accept u svakoj clasi :D
