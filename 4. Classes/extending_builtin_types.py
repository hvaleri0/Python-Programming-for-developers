# extended Test to string "str" type
class Text(str):
    def duplicate(self):
        return self + self


# extended Trackable List to list class
class TrackableList(list):
    # redefine the internal append method
    def append(sel, object):
        print("Append called")
        super().append(object)


text = Text("Python")
# inherits all the str method plus the custom defined method "duplicate"
print(text.lower())
print(text.duplicate())

list = TrackableList()
list.append("1")
