class Point:
    def __init__(self, x, y):  # Magic method
        self.x = x
        self.y = y

    def __str__(self):  # Magic Method to display obeject as string
        return f"({self.x},{self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point)  # by default get the address of this point object in memory if we define __st__ we can sho it howwe want it
