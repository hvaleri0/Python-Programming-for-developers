# Example of a programmers mistake: Exception due to list index out of range
numbers = [1, 2]
print(numbers[3])


# Example of a bad data from user: Exception if user inputs wrong type of data
age = int(input('Age: '))  # if user enter a string we get an exception
