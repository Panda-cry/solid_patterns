#Abstractions should not depend upon details.
#Details should depend upon abstractions.


# app_dip.py

from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"


# Sta je cilj ovde da ne trebam da zavisim od konkretnih klasa
# nego do apstrakcje
# jer svaka naslednica implementira apstraktnu klasu
# i nema zavisnosti
# kao sto vidimo get_data metod mozemo da zovemo i sa api i sa database :D
# zavisi od toga sta nam treba :D