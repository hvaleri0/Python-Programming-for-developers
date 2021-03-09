from pathlib import Path
from zipfile import ZipFile

# To Create:
# Create a zip file named file.zip and "w" for write
# use with-for to avoid try-catch in case of errros and to close the file at the end
with ZipFile('files.zip', "w") as zip:
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)

# To Read:
with ZipFile("files.zip") as zip:
    print(zip.namelist())  # return the list of all files in the zip file
    info = zip.getinfo("ecommerce/__init__.py")  # get file info
    print(info.file_size)  # attribute of getinfo
    print(info.compress_size)  # attribute of getinfo
    # used to extract all file, optional name of directory "extract" folder:
    zip.extractall("extract")
