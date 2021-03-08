# import the Path Class:
from pathlib import Path

# absolute path:
# For Window Users:
Path("C:\\Proram Files\\Microsoft")

# use Raw string to get rid of second backslashes:
Path(r"C:\Program Files\Microsoft")

# For Mac and Linux Users:
Path("/usr/local/bin")

# Use current Folder:
Path()

# Relative paths:
Path("ecommerce/__init__.py")

# You can combine objects together:
Path()/Path("eccomerce")

# You can combine path object with a string:
Path()/"ecommerce"/"__init__.py"

# Get home directory of current user:
Path.home()

# Start Demo Here
path = Path("ecommerce/__init__.py")

# Methods for validation
path.exists()  # check if it exist
path.is_file()  # check if its a file
path.is_dir()  # check if its a dir

# Attributes
print(path.name)  # provide file name
print(path.stem)  # provide file name w/o extention
print(path.suffix)  # provide file extension
print(path.parent)  # provide file parent

# Methods for Action
path = path.with_name("file.txt")  # create new  path object with existing path
print(path.absolute())  # get the absolute value of the path
path = path.with_suffix(".py")  # change extention of the path suffix
print(path)  # get the absolute value of the path
