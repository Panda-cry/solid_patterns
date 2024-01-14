# Metaklasa sluzi da definise nacin na koji ce se
# kreirati objekat
# sve klase u pyhonu su objekti
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Ako menjano nesto tj imamo __init__
        Takodje __call__ ne zavisi od init-a klase koja nasledjuje
        Tako da smo zasticeni :D"""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def some_logic(self):
        pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    if s1 == s2:
        print("Singleton works, both variable have same instance")
    else:
        print("Something is broke :D")

