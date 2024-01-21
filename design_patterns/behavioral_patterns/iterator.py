from collections.abc import Iterator, Iterable
from typing import Any


class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection, reverse: bool = False):
        self.collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):

        try:
            value = self.collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):

    def __init__(self, collection =None):
        self.collection = collection or []

    def __getitem__(self, item):
        return self.collection[item]

    def __iter__(self):
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self):
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item):
        self.collection.append(item)


if __name__ == "__main__":
    # The client code may or may not know about the Concrete Iterator or
    # Collection classes, depending on the level of indirection you want to keep
    # in your program.
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")


#kreiramo iterator nekih svojih objekata kako mozemo da ih obilazimo
# ako imamo neki specifican slucaj obilaska npr