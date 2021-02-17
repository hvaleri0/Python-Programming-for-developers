# use try blocks to handle exceptions.
try:
    age = int(input('Age: '))
except ValueError as ex:  # you can use Alias to define a varianble
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("no exceptions were thrown")
print('Excecution continues.')
