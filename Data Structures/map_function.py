items = [  # name and Price
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

# lets say we want to transform it to prices only:
prices = []
for item in items:
    prices.append(item[1])

print(prices)

# mapfunction is more elegant;
x = map(lambda item: item[1], items)
for item in x:
    print(item)

# use list to further simplify:
prices = list(map(lambda item: item[1], items))
print(prices)
