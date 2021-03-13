import random
import string

print(random.random())  # generates a number between 0-1
print(random.randint(1, 10))  # generates an int between 2 int
print(random.choice([1, 2, 3, 4]))  # selects one value from array randomly
# selects k number of value from array randomly:
print(random.choices([1, 2, 3, 4], k=2))
# generate a random passsword of 4 characters:
print("".join(random.choices("abcdefg", k=4)))

# more effective solution is to use the asci attribute from string module:
print(string.ascii_letters)
print("".join(random.choices(string.ascii_letters+string.digits, k=8)))

# useful method for shufeling an array:
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
