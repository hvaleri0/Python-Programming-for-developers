class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("person Greet")


# method & attibute would be pick sequentially :1:Manager, 2:Employee, 3: Person
class Manager(Employee, Person):
    pass


m = Manager()
# solution: "Employee Greet" will print beware of sequence in multiple inhritance
print(m.greet())
