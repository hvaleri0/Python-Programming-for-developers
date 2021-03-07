class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        # if we didnt have super() we would be replacing as oppose to extending the method
        super().__init__()  # you can move the order of this implementation
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
