from abc import ABC, abstractmethod
from random import random, randrange, randint
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteSubject(Subject):
    _state: int = 0

    _observers: List = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def some_logic(self):
        self._state = randint(0, 10)
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        pass


class ConcreteObserver1(Observer):
    def update(self, subject):
        if subject._state < 5:
            print("Observer 1")


class ConcreteObserver2(Observer):

    def update(self, subject):
        if subject._state >= 5:
            print("Observer 2")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer1 = ConcreteObserver1()
    observer2 = ConcreteObserver2()
    subject.attach(observer1)
    subject.attach(observer2)

    for _ in range(3):
        subject.some_logic()

    subject.detach(observer1)

    for _ in range(5):
        subject.some_logic()


# Imamo neke subskripcije gde se na poziv jedne metode pozivaju svi
# koji se nalaze u listi
# tako da notifikujemo sve koji su subscribed i onda oni kasnije vrse neke akcije
# na osnovu stanja subject-a :D