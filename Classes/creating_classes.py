class Point:
    def draw(self):  # all function shall haveatleast one param
        print("draw")


point = Point()  # create an instance of the Point class
print(type(point))
# check to see if the point object is an instance of the Point class
print(isinstance(point, Point))
