class Animal:
    def __init__(self):
        self.age = 1

    def eat(sef):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub-Base


class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, object))
print(issubclass(Mammal, object))
