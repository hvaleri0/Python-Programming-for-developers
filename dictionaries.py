# Dictionaries can be define like this:
point = {'x': 1, 'y': 2}
# or Can be defined witht he dict function * preffered way:
point = dict(x=1, y=2)

# to get a value of a key in a dictionary:
print(point["x"])

# to change a value of a key in a dictionary:
point['x'] = 10
print(point)

# to add a new key-value to dictionary:
point['z'] = 20
print(point)


# if value is not found you get an error make sure to address it by checking for availability
# sol 1: check first
if "a" in point:
    print(point["a"])
# sol 2: the Get Method, can explictly state what to return if not found.
print(point.get('a', 0))

# to delete use the Del function:
del point['x']
print(point)

# how to loop over dictionary
# Option 1:
for key in point:
    print(key, point[key])
# Option 2:
for key, value in point.items():
    print(key, value)
