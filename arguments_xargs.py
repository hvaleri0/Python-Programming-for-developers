def multiply(*list):  # use Asterik to make it a tupple , tuples are iterable
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 5, 6))
