letters = ['a', 'b', 'c']
if "d" in letters:
    # ValueError: 'd' is not in list if no if statement
    print(letters.index('d'))

# Another way to find out if the letter exist is with count:
print(letters.count('d'))
