class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken (Bird):  # Error: Chicken cant fly!
    pass  # use pass to execute code withoput error if empty block needed
