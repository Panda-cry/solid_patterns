from abc import ABC, abstractmethod
from typing import List


class Component(ABC):

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def is_composite(self) -> bool:
        return False

    def operation(self) -> str:
        pass


class Leaf(Component):

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):

    def __init__(self):
        self._children: List[Component] = []

    def add(self, component):
        self._children.append(component)
        component._parent = self

    def remove(self, component):
        self._children.remove(component)
        component._parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        result = []

        for child in self._children:
            result.append(child.operation())

        return f"Branch({'+'.join(result)})"


def client_code(component: Component):
    print(f"RESULT: {component.operation()}")


def client_code_2(component1: Component, component2: Component):

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}")


if __name__ == "__main__":

    simple = Leaf()

    three = Composite()

    branch1 = Composite()
    branch2 = Composite()

    branch1.add(Leaf())
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2.add(Leaf())

    three.add(branch1)
    three.add(branch2)

    client_code(three)

#Koristi se kada imamo neku hijarahiju