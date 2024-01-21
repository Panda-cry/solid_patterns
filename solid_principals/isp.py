# Clients should not be forced to depend upon methods that they do not use.
# Interfaces belong to clients, not to hierarchies.
from abc import ABC, abstractmethod


class Printer(ABC):

    @abstractmethod
    def printt(self):
        pass

    @abstractmethod
    def fax(self):
        pass


class OldPrinter(Printer):

    def printt(self):
        pass

    def fax(self):
        pass


class NewPrinter(Printer):

    def printt(self):
        pass

    def fax(self):
        pass


# Ovde se narausava ISP jer stari stampac nema fax
# potrebno razdovojiti interfejse

# printers_isp.py

from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")


class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
