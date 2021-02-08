# whever we see the following algo use comprehension!
values = []
for x in range(5):
    values.append(x*2)
print(values)

# remember: [Expression for item in items]
values2 = [x*2 for x in range(5)]
print(values2)

# Can use same with sets by replacing [] with {}
values3 = {x*2 for x in range(5)}
print(values3)

# sytactical difference between a set and a dictionary:
# - sets only have values:
{1, 2, 3, 4}
# - dictionaries have keyvalue pairs:
{1: "a", 2: "b", 3: "c"}

# Now to use comprehension in dictionaries:
values4 = {x: x*2 for x in range(5)}
print(values4)
