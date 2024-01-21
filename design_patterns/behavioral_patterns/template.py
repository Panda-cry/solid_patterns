from abc import ABC, abstractmethod


class AbstractClass(ABC):

    def template_method(self):
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.required_operation2()

    def base_operation1(self):
        print("!1")

    def base_operation2(self):
        print("!2")

    def base_operation3(self):
        print("!3")

    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def required_operation2(self):
        pass


class ConcreteClass1(AbstractClass):

    def required_operation1(self):
        print("#1")

    def required_operation2(self):
        print("#2")


if __name__ == "__main__":
    concrete_class = ConcreteClass1()

    concrete_class.template_method()

#Template sluzi da imamo abstraktnu klasu gde definisemo metode koje cemo koristiti
# koristimo jednu metodu koja ostale stvari radi za nas
# klase koje nasledjuju mogu a ne moraju da implementiraju sve metode tj da redefinisu
