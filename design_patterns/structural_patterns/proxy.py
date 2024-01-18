from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):

    def request(self):
        print("RealSubject: Handling request.")


class Proxy(Subject):

    def __init__(self, real_subject: RealSubject):
        self._real_subjetc = real_subject

    def request(self):
        if self.check_access():
            self._real_subjetc.request()
            self.log_access()

    def check_access(self):
        print("We checked access")
        return True

    def log_access(self):
        print("Logged !!!")


def client_code(subject: Subject):
    subject.request()


if __name__ == "__main__":
    real_subject = RealSubject()
    client_code(real_subject)

    print("\n\n")

    proxy = Proxy(real_subject)
    client_code(proxy)

# Sve u svemu presecemo request i proveravmo
# Slicno je kao dekorator samo sto je dekorator u sluzbi klijenta
# Dok je proxy u sluzbi servisa
