items = [  # name and Price
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]
prices = list(map(lambda item: item[1], items))  # with map function
prices_le = [item[1] for item in items]  # list expression mapping
print(prices_le)

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered_le = [item for item in items if item[1] >= 10]
print(filtered_le)
