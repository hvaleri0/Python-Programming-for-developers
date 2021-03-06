try:
    file = open(cleanup.py)
    age = int(input('Age: '))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):  # multiple ecseptions in one clause
    print("You didn't enter a valid age.")
else:
    print("no exceptions were thrown")
finally:
    # use finally to excue alway (with or withour Exceptions) best used to close network connections, files, or DB
    file.close()
