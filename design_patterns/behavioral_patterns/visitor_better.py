from abc import ABC, abstractmethod


class Visitor(ABC):

    @abstractmethod
    def calculate_shape_triangle(self, element):
        pass

    @abstractmethod
    def calculate_shape_circle(self, element):
        pass


class Shape(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def accept(self, visitor):
        visitor.calculate_shape_triangle(self)


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor: Visitor):
        visitor.calculate_shape_circle(self)


class ConcreteVisitor(Visitor):

    def calculate_shape_triangle(self, element):
        print(element.a + element.b + element.c)

    def calculate_shape_circle(self, element):
        print(f"Circle have {element.radius * 2 * 3.14}")


def client(components: list, visitor: Visitor):
    for component in components:
        component.accept(visitor)


if __name__ == "__main__":
    components = [Circle(12), Triangle(1, 2, 3)]

    visitor = ConcreteVisitor()

    client(components, visitor)
