from timeit import timeit  # used to calculate execution time of code

# use triple quotes when code expanded to multiple lines & Pass statement when you want code to do nothing
code1 = """ 
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be 0 or less.")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    # print(error)
    pass
"""

code2 = """ 
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    # print(error)
    pass
"""

print("First Code=", timeit(code1, number=10000))
print("Second Code=", timeit(code2, number=10000))
