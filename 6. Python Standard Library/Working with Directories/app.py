from pathlib import Path

path = Path("ecommerce")

# path.exists()  # returns a bool for existence
# path.mkdir()  # to create this directory
# path.rmdir()  # to remove the directory
# path.rename("ecommerce2")  # to rename to a new name

for p in path.iterdir():  # get list of files and directories in a path. generator obeject needs to be in a loop
    print(p)

# use list comprehension expresion if you know the files and directories:
paths = [p for p in path.iterdir()]
print(paths)

# we can apply filtering to the comprehension expression
paths = [p for p in path.iterdir() if p.is_dir()]

# use Glob for patterns
py_files = [p for p in path.glob("*.py")]

# to search recursivelly 2 ways:
py_files = [p for p in path.glob("**/*.py")]  # manual
# use the rglob short for recursive glob
py_files = [p for p in path.rglob("*.py")]

print(py_files)
