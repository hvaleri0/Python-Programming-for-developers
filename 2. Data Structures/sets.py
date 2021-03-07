numbers = [1, 1, 2, 3, 4]

# if you want to remove duplicates you can convert to a set:
first = set(numbers)

# use curly braces to define a set:
second = {1, 4, 5, 6}
second.add(5)
second.remove(5)
len(second)
print(first)

# power Math operations
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

# cannot access using index:
print(first[0])

if 1 in first:
    print('yes')
