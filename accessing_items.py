letters = ['a', 'b', 'c', 'd']
letters[0] = 'A'
print(letters[::3])  # Skip till 3rd item
print(letters)  # does not modify original

numbers = list(range(20))
print(numbers[::2])  # print every 2nd item

print(numbers[:: -1])  # print in reverse order
