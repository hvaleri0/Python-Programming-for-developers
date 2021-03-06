# old School
names = ["John", "Mary"]
found = False
for name in names:
    if name.startswith("L"):
        print("Found")
        found = True
        break  # terminate iteration once found
if not found:
    print("Not found")

# Cleaner Way with python with for else:
names = ["John", "Mary"]
for name in names:
    if name.startswith("L"):
        print("Found")
        break  # terminate iteration once found
else:
    print("Not found")
