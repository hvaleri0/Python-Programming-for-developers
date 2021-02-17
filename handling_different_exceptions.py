#  You can add multiple exception or add multiple times of exception into one clause
try:
    age = int(input('Age: '))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):  # multiple ecseptions in one clause
    print("You didn't enter a valid age.")
except ZeroDivisionError:  # will not run because previous exception handles it
    print("Age cannot be 0.")
else:
    print("no exceptions were thrown")
