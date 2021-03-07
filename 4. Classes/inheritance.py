# Animal: Parent, Base
class Animal:
    def __init__(self):
        self.age = 1

    def eat(sef):
        print("eat")


# Mammal: Child, Sub-Base
class Mammal(Animal):
    def walk(self):
        print("walk")


# Fish: Child, Sub-Base
class Fish(Animal):
    def swim(self):
        print('swim')


m = Mammal()
m.eat()
print(m.age)
