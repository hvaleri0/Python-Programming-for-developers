from abc import ABC, abstractmethod
# if it walks like a duck and quacks like a duck, it is a duck!


class TextBox:
    def draw(self):
        print('TextBox')


class DropDownList:
    def draw(self):
        print('DropDownList')


# python is a dymanic language as long as controls is iterable and the draw method is available it wont fail
def draw(controls):
    for control in controls:
        control.draw()


# However it is good practice to inforce abstraction so that you inforce the contract or interface.
ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])
