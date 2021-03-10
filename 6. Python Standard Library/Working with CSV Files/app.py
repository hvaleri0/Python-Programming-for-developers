import csv

# to Create:
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([100, 1, 5])
    writer.writerow([101, 2, 15])

# To Read:
with open("data.csv") as file:
    reader = csv.reader(file)
    # reader returns string so need to convert to interger, float and so on if needed.
    # print(list(reader)) # wont run for loop if uncomment because of index position
    for row in reader:
        print(row)
