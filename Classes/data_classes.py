from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])

p1 = Point(x=1, y=2)
# tuples are immutable cannot xange once defined eg. p1.x =3
# to reassign use
p1 = Point(x=10, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)  # no need to define the __eq__ magic method
