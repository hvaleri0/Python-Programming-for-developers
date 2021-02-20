try:
    # Can open multiple external resource at once by seperating with  commas.
    with open("cleanup.py") as file, open("anotherFile.txt") as target:
        print("File opened.")

    age = int(input('Age: '))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):  # multiple ecseptions in one clause
    print("You didn't enter a valid age.")
else:
    print("no exceptions were thrown")
