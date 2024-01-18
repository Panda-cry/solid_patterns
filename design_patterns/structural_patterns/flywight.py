import json
from typing import Dict


class Flyweight:

    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Shared state {s}")
        print(f"Unique state {u}")


class FlyweightFactory:
    _flyweights = {}

    def __init__(self, initial_flyweigts):
        for state in initial_flyweigts:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state):
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state):

        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("We need to add it")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("We have it ")

        return self._flyweights[key]

    def list_flyweights(self):

        count = len(self._flyweights)

        print(f"We contain {count} items in dict")
        print("\n".join(map(str, self._flyweights.keys())))


def add_car_to_database(factory: FlyweightFactory, plates, owner, brand, model,
                        color):
    flyweight = factory.get_flyweight([brand, model, color])

    flyweight.operation([plates, owner])


if __name__ == "__main__":

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()


    add_car_to_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()

#Cuvamo bitne podatke sto su jedinstvene a ove sto se menjaju i ne bas
# OVo je slicno nesto kao 4 normalne forme :D