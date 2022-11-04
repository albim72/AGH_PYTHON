class MojaMeta(type):

    def __new__(cls, clsname, superclass, attibutedict):
        print(f"nazwa klasy: {clsname}")
        print(f"dziedziczone klasy: {superclass}")
        print(f"atrybuty klasy: {attibutedict}")
        return type.__new__(cls,clsname, superclass, attibutedict)


class Pierwsza:
    pass

class Glowna(Pierwsza,metaclass=MojaMeta):
    pass

class Druga(Glowna):
    pass
