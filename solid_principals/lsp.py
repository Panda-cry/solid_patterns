
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        # Pozivamo konstruktor nadklase sa istom vrednošću za širinu i visinu
        super().__init__(side, side)

# Koristimo objekat nadklase
rectangle = Rectangle(4, 5)
print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 20

# Koristimo objekat podklase
square = Square(4)
print(f"Square Area: {square.area()}")  # Output: Square Area: 16

# Ako je S potklasa T, onda objekti tipa T mogu biti zamenjeni objektima tipa S
# , a da se ne naruši ispravnost programa.
# Specifikacija podklase: Podklasa mora proširiti
# specifikaciju (ponašanje) nadklase,
# a ne je suziti.
# Ovo znači da metode podklase treba da pruže bar
# istu funkcionalnost kao i metode nadklase.