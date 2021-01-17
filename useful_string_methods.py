course = "  Python Programming  "
print(course.upper())  # Upper Case
print(course.lower())  # Lower Case
print(course.title())  # Upper Case first char of wach word

# Remove whitespace from begining and end of obj str can use .lstrip() or rstrip() for begining or end of obj str
print(course.strip())

# find index location of a character or word note -1 is a not found result
print(course.find('Pro'))

print(course.replace("P", "-"))  # Replace Characters

# check for the existance or sequence of character, returns a bool
print("Programming" in course)

print("Programming" not in course)  # Not operator
