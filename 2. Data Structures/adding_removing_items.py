letters = ['a', 'b', 'c']

# Add
letters.append('d')
letters.insert(0, '-')
print(letters)


# Remove
letters.pop()
letters.pop(0)
letters.remove('b')  # Removes first occurence of letter 'b'
del letters[0:1]  # del is useful when deleting a range
letters.clear()  # to remove all objects in list
print(letters)
