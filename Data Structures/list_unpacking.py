numbers = [1, 2, 34, 4, 4, 4, 4, 4, 4, 4, 94]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# cleaner much easier way:
# first, second, third = numbers

# What if we want only the 1st and 2nd items:
first, second, *others = numbers  # pack the rest in *others

# what if we want the first and last item:
first, *other, last = numbers  # pack the middle in *others
print(last)
