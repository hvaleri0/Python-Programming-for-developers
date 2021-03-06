class Point:
    def __init__(self, x, y):  # self is a reference to the current object
        self.x = x
        self.y = y

    def draw(self):  # all function shall have atleast one param
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)  # create an instance of the Point class
point.draw()  # technically you would call point.draw(point) to refence self but no need
