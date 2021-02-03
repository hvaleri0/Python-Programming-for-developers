items = [  # name and Price
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]


# def sort_item(item):
#     return item[1]  # sort by price

# lambda function is a one line ananymous function that can bepassed to another function, use it to simplify sort code:
#Syntax: lambda parameter:expression
items.sort(key=lambda item: item[1])
print(items)
