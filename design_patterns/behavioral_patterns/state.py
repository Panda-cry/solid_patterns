from abc import ABC, abstractmethod

class Context:
    _state = None

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        print(f"Context state change to {state.__class__.__name__}")
        self._state = state
        self._state.context = self

    def request_1(self):
        self._state.handle_1()

    def request_2(self):
        self._state.handle_2()


class State(ABC):

    @property
    def content(self) -> Context:
        return self.context

    @content.setter
    def content(self, content : Context) -> None:
        self.contex = content

    @abstractmethod
    def handle_1(self):
        pass

    @abstractmethod
    def handle_2(self):
        pass





class ConcreteState1(State):

    def handle_1(self):
        print("Concrete State 1 handle and switch")

        self.content.transition_to(ConcreteState2())

    def handle_2(self):
        print("Concrete state 1 handle request 2")


class ConcreteState2(State):

    def handle_2(self):
        print("State 2 switch to 1 ")
        self.content.transition_to(ConcreteState1())

    def handle_1(self):
        print("State 2 something")


if __name__ == "__main__":
    context = Context(ConcreteState1())
    context.request_1()
    context.request_2()


# Razlika izmedju state i strategy je ta sto state zna za druga stanja
# koristiti kada imamo dosta stanja i da zamenimo te if vrednosti 