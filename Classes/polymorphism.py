from abc import ABC, abstractmethod


class UIControl(ABC):  # only defines the contract or interface that all derivatives should follow
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print('TextBox')


class DropDownList(UIControl):
    def draw(self):
        print('DropDownList')


# our draw method takes many different forms
def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])
