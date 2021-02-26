class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(1, 2)
other = Point(1, 2)
# if we dont define the __eq__ magic method, it will be false
# because here we are comparing the object address in memeory which is not the same
print(point != other)
print(point > other)
# python automatically defiines less than because greater than was defined
print(point < other)
