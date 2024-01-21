from abc import ABC


class Mediator(ABC):

    def notify(self, sender, event):
        pass


class ConcreteMediator(Mediator):

    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:

    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator


class Component1(BaseComponent):

    def do_a(self):
        print("Do a")
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Do B")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):

    def do_c(self):
        print("Do C")
        self.mediator.notify(self, "C")

    def do_d(self):
        print("Do D")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    c1 = Component1()
    c2 = Component2()

    mediator = ConcreteMediator(c1, c2)

    c1.do_a()

    c2.do_d()

# Jednostavno kreiramo klasu koja ce da poziva i vraca sta treba ostalima
# Kao neki service bus da kreiramo
# da bi izbegli zavisnosti klasa i kompozicije razne :D
