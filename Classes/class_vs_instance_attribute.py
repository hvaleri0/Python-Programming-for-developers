class Point:
    default_color = "red"  # class level attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"  # change default color of class to yellow

point = Point(1, 2)
print(point.default_color)  # read Object attibute
# read Class attibute note that "Point" is the class
print(Point.default_color)
point.draw()

another = Point(3, 4)  # intance level attribute
# color attribute change in Class made its way to the instance attribute
print(another.default_color)
another.draw()
