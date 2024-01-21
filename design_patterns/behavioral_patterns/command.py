from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class SimpleCommand(Command):

    def __init__(self, payoad):
        self.payload = payoad

    def execute(self):
        print(f"Simple {self.payload}")


class ComplexCommand(Command):

    def __init__(self, receiver, a, b):
        self.receiver = receiver
        self.a = a
        self.b = b

    def execute(self):
        print("Complex")
        self.receiver.do_something(self.a)
        self.receiver.do_something_else(self.b)


class Receiver:

    def do_something(self, a):
        print(f"Receiver got {a}")

    def do_something_else(self, a):
        print(f"Receiver something else {a}")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command):
        self._on_start = command

    def set_on_finish(self, command):
        self._on_finish = command

    def do_something_important(self):
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    invoker = Invoker()

    invoker.set_on_start(SimpleCommand("Bruka"))
    receiver = Receiver()

    invoker.do_something_important()

# Omogucava da dovojimo izvrsenje od klase
# npr radice nam klase resenje a ne jedna klasa da radi sve
# Sama rec komanda daje nam na znanje da imamo jednu klasu koja zadaje komande kao neki ifovi
# fje koje pozivaju druge komande za radi i resavanje problema
# tipa primer je kalkulator :D undo redo itd