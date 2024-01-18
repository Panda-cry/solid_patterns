class Target:

    def request(self):
        return "data request"


class Adaptee:

    def specific_request(self):
        return "Data Request"


class Adapter(Target, Adaptee):

    def request(self):
        return self.specific_request()


def client(target: Target):

    print(target.request())


if __name__ == "__main__":
    target = Target()
    client(target)

    adapter = Adapter()
    client(adapter)



#Fora je jednostavna
#Kreiramo klasu koja ce da override metodu roditelja
#I iskoristiti metodu 2 Roditelja
#tako da poziv ostaje isti dok rezultat nije 