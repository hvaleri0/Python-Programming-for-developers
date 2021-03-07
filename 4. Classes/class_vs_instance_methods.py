class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod  # Class Method: Ad decorator 'classmethod' and "cls" to define as class method
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")  # instance Methods


point = Point.zero()  # class method are useful when initializing complex objects
point.draw()
