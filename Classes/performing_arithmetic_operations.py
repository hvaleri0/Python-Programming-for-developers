class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # add arithmetic method
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)

combined = point + other  # comnbines the object based on the __add__ implementation
print(combined.x)
