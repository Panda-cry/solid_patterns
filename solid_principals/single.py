# Klasa treba da ima samo jednu odgovornost
# Jedan zadatak klase resavamo pomocu vise metoda
# Ako se doda jos neki zadatak odvojiti ga u susednu klasu

# File manager

class FileManager:

    def __init__(self, path):
        self.path = path

    def read(self, encoding):
        pass

    def write(self):
        pass

    def compress(self):
        pass

    def decompress(self):
        pass


class FileManager:

    def __init__(self, path):
        self.path = path

    def read(self, encoding):
        pass

    def write(self):
        pass


class ZipManager:

    def compress(self):
        pass

    def decompress(self):
        pass
