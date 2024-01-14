import copy


class SelfReferencingEntity:

    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:

    def __init__(self, some_int, some_list, some_circular_ref):
        self.int = some_int
        self.list = some_list
        self.ref = some_circular_ref

    def __copy__(self):
        some_list_copy = copy.copy(self.list)
        some_ref = copy.copy(self.ref)

        new = self.__class__(
            self.int, some_list_copy, some_ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memodict={}):
        some_list_copy = copy.copy(self.list)
        some_ref = copy.copy(self.ref)

        new = self.__class__(
            self.int, some_list_copy, some_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memodict)

        return new


if __name__ == "__main__":
    list_ints = [1,2,3,4]
    circulare_ref = SelfReferencingEntity()
    component = SomeComponent(23,list_ints,circulare_ref)
    circulare_ref.set_parent(component)


    copied_component = copy.copy(component)

    copied_component.list = []

    if len(component.list) == 0:
        print("I ovde je uklonjeno")
    else:
        print("Malo morgen nije")


    deep_copy = copy.deepcopy(component)

    deep_copy.list.append(5)
    if 5 in component.list:
        print("Dodali smo i ovde")
    else:
        print("E pa nismo bas")

    print(f"Ref from component {copied_component.ref}")
    print(f"Ref from clone {copied_component.ref}")
    print(f"Ref from deep_clone {deep_copy.ref}")

#prototype omogucava da se objetki kloniraju
#bez da se petlja oko klase ili ostalog mozemo da kopiramo bilo sta
