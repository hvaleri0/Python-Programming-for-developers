letters = ['a', 'b', 'c']

# recall you can also unpack topple:
items = (0, 'a')
a, b = items

# use unpack inside a for loop:
# for letter in letters:
for index, letter in enumerate(letters):
    print(index, letter)
