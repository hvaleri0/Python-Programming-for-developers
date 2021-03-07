numbers = [3, 51, 2, 8, 6]
# numbers.sort() # sort original ascending
# numbers.sort(reverse=True)  # sort original descending
print(sorted(numbers))  # new list sorted ascending and keeping original
# new list sorted descending and keep original:
print(sorted(numbers, reverse=True))
print(numbers)

items = [  # name and Price
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]


def sort_item(item):
    return item[1]  # sort by price


items.sort(key=sort_item)
print(items)
