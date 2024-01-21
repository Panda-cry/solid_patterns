from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):

    @abstractmethod
    def do_something(self, data: List):
        pass


class Context:

    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_some_logic(self):
        print(f"Storing data using strategy - {self._strategy.__class__.__name__}")
        result = self._strategy.do_something(['a', 'b', 'c'])
        print(result)


class ConcreteStrategy1(Strategy):

    def do_something(self, data: List):
        return "+".join(data)


class ConcreteStrategy2(Strategy):

    def do_something(self, data: List):
        return  "-".join(data)


if __name__ == "__main__":

    context = Context(ConcreteStrategy1())

    context.do_some_logic()

    context.strategy = ConcreteStrategy2()

    context.do_some_logic()



# imamo jedan interfejs/ klasu koja ima polje strategija i gde ubacujemo zeljenu strtegiju
# nakon cega izvrsavamo neku logiku
# strategiju koristiti kada imamo neki problem koji se resava na vise nacina
# gde mozemo da koristimo 1 metodu da pozivamo i menjamo strategije resavanja problema
# strategije ne znaju jedna za drugu!!!