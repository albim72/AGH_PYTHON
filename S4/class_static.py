from datetime import date

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def ile_od_narodzin(cls,name,year):
        return cls(name,date.today().year-year)

    @staticmethod
    def czydosrosly(age):
        return age >= 18


pr1 = Person('Roman',24)
pr2 = Person.ile_od_narodzin('Anna',1981)

print(pr1.age)
print(pr2.age)

print(pr1.czydosrosly(pr1.age))
print(pr2.czydosrosly(pr2.age))
print(Person.czydosrosly(age=67))
print(Person.ile_od_narodzin("Tytus",1954))
