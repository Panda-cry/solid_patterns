from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters


class Originator:
    _state = None

    def __init__(self, state):
        self._state = state

        print(f"Originator: My initial state is: {self._state}")
    def do_something(self):
        print("Originator: I'm doing something important")

        self._state = self.generate_random_string(30)
        print(f"Originator changed state {self._state}")

    @staticmethod
    def generate_random_string(self, length: int = 10):
        return "".join(sample(ascii_letters, length))

    def save(self):
        return ConcreteMomento(self._state)

    def restore(self, momento):
        self._state = momento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Momento(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_state(self):
        pass


class ConcreteMomento(Momento):

    def __init__(self, state: str):
        self._state = state
        self._date = str(datetime.now())

    def get_state(self):
        return self._state

    def get_name(self):
        return f"{self._date} / {self._state}"

    def get_date(self):
        return self._date


class Caretaker:

    def __init__(self, originator: Originator):
        self.momentos = []
        self._originator = originator

    def backup(self):
        print("We will save it")
        self.momentos.append(self._originator.save())

    def undo(self):
        if not len(self.momentos):
            return

        momento = self.momentos.pop()

        print(f"Caretaker restore momento {momento.get_name()}")
        try:
            self._originator.restore(momento)
        except Exception:
            self.undo()

    def show_history(self):

        for momento in self.momentos:
            print(momento.get_name())


if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()



#Sve u svemu glavnu ulogu ima momento jer on cuva stanje originala
# original ima pozive vrati i sacuvaj jedan momento
# kasnije caretaker samo ima undo redo
# gde vracamo prethodni momento i on objektu ponovo setuje stanje
# nije nesto komplikovano :D