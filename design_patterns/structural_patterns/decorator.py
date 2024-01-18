class Component:

    def operation(self):
        pass


class ConcreteComponent(Component):

    def operation(self):
        print(f"Concrete Component :D")


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component):
        self._component = component

    @property
    def component(self):
        return self._component

    def operation(self):
        return self.component.operation()


class ConcreteDecoratorA(Decorator):

    def operation(self):
        print("Concrete Decorator A")
        self.component.operation()


if __name__ == "__main__":

    component = ConcreteComponent()

    decorator = ConcreteDecoratorA(component)

    decorator.operation()


#Dekorator nije kao Aadapter
#glavna razlika je jer se ovde radi o jednom proizvodu
#U adapteru treba da uklopimo 2 razlicita
#OVde su komponente iste
#U apdateru je drugacija metoda !!!