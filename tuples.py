point = (1, 2, 3)  # tupple
point1 = 1, 2  # tupple default if no parentesis present
point2 = 1,  # tupple, trailing coma
point3 = ()  # empty tupple
point4 = (1, 2)+(3, 4)  # tupple concatanate
point5 = (1, 2)*3  # tupple Repeat

point6 = tuple([1, 2, 3])  # convert list to tuple
point6 = tuple("Hello World")  # convert list to tuple


print(type(point1))
print(point6)

# accesing tuples:
print(point4[0])  # using index
print(point4[0:2])  # using Range to access

x, y, z = point  # unpacking tupple

# finding values in tuples
if 3 in point:
    print('3 Exists')
