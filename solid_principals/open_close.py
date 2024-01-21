# Open close klasa bi trebala da bude otvora za
# kreiranje novih vrsta ali ne i za modifikaciju

class Model:

    def __init__(self, shape, **kwargs):
        self.shape = shape
        if shape == "rectangle":
            self.a = kwargs['a']
            self.b = kwargs['b']

        if shape == "circle":
            self.radius = kwargs['radius']

    def calculate_area(self):
        if self.shape == "circle":
            return
        if self.shape == "rectangle":
            return


from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, shape):
        self.shape = shape

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):

    def calculate_area(self):
        pass


class Square(Shape):

    def calculate_area(self):
        pass


class Circle(Shape):

    def calculate_area(self):
        pass
