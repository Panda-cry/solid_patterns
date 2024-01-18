class System1:

    def operation1(self):
        print("Operation 1")

    def operationN(self):
        print("Operation N")


class System2:

    def operation2(self):
        print("Operation 2")

    def operationZ(self):
        print("Operation Z")


class Facade:

    def __init__(self, system1: System1, system2: System2):
        self.system1 = system1
        self.system2 = system2

    def operation(self):
        self.system1.operation1()
        self.system2.operation2()
        self.system1.operationN()
        self.system2.operationZ()


if __name__ == "__main__":
    facade = Facade(System1(), System2())
    facade.operation()


#Kada zelimo da predstavimo neki interfejs koji povezuje dosta slozenih stvari
#a vracamo nesto easy