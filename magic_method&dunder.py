# magic methods and Dunder - Advance python programming


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object is being deconstructored")

p = Person("Ganesh",25)