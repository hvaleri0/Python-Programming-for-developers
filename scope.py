# Local
def greet():  # define variable in local function
    if True:
        message = "a"  # does not matter if defined in an if statement, still local to the function
    print(message)


print(greet())


# Global
message = 'b'


def greet2():
    global message  # use to call for Global
    message = "c"


print(greet2())
print(message)

# Avaoid Global its bad practice , it evil!
