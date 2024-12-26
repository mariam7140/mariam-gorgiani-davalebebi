class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age_name(self):
        return f"Name: {self._name}, Age: {self._age}"

person1 = Person("Mari", 25)
person2 = Person("Nino", 30)
person3 = Person("Nika", 22)


print(person1.get_age_name())
print(person2.get_age_name())
print(person3.get_age_name())
