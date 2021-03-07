def multiply(*numbers):  # use Asterik to make it a tupple , tuples are iterable
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(multiply(2, 3, 5, 6))
print("Finish")

# Debug Hot Keys
# fn+5 -> start
# fn+10 -> step over
# fn+11 -> step in
# fn+shift+11 -> step out
