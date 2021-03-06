# defining by default parameters and adding annotation
def increment(number: int, by: int = 1) -> tuple:
    return (number, number+by)


print(increment(2, by=3))  # keyword argument "by"
print(increment(2))
