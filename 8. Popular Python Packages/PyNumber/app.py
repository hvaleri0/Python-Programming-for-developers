import numpy as np

array = np.array([1, 2, 3])
print(array)  # = [1 2 3]
print(type(array))  # = <class 'numpy.ndarray'>

# multidimensional array:
array = np.array([[1, 2, 3], [2, 5, 6]])  # 2 dimentional array: Matrix
print(array)  # = [[1 2 3] n/ [2 5 6]]
print(array.shape)  # = (2, 3) : 2 rows 3 columns

# helper function for initiallizing arrays:
# creates an 3X4 matrix initialized with 0 (int type):
array = np.zeros((3, 4), dtype=int)
print(array)

# creates an 3X4 matrix initialized with 1 (int type):
array = np.ones((3, 4), dtype=int)
print(array)

# creates an 3X4 matrix initialized with custom number (int type):
array = np.full((3, 4), 8, dtype=int)
print(array)

# creates an 3X4 matrix initialized with Random number (int type):
array = np.random.random((3, 4))
print(array)

# access individual arrays by index
print(array[0, 0])

# extremelly powerful you can test bool expresion:\
print(array > .4)

# extremelly powerful you can calc bool indexing:\
print(array[array > 0.4])

# computational methods:\
print(np.sum(array))
print(np.floor(array))
print(np.ceil(array))
print(np.round(array))

# arithmetic operations between Arrays and numbers:
first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print(first + second)  # all operations available
print(first + 2)

# Real life example: Convert to inch to cm
# Implementation in Numpy * Much simple
dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)

# implementation in pure python
dimensions_inch_ = [1, 2, 3]
dimensions_cm_ = [x*2.54 for x in dimensions_inch]
print(dimensions_cm_)
