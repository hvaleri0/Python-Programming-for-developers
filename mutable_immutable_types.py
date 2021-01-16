# x = 1 # immutable
x = [1, 2, 3]  # mutable
print(id(x))

# x = x + 2
x.append(4)
print(id(x))
