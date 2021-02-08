numbers = [1, 2, 3]

# Unpacking operator -> "*" similar to Javascript -> "..."
print(*numbers)


# unpacking operator can unpack any iterable includes range!
values = [*range(5)]
print(values)

# can unpack strings as well:
values = [*range(5), *"Hello World"]
print(values)

# you can combine list;
first = [1, 2, 3]
second = [10, 20, 40]
values = [*first, *second]
print(values)


# you can combine dictionaries;
first = {'x': 1, 'y': 3}
second = {'x': 10, 'z': 40}  # x is override to 10
values = {**first, **second, "j": 30}  # you can add additional keyvalues
print(values)
