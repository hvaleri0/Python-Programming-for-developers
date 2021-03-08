from pathlib import Path
from time import ctime  # convert epoch to human
import shutil  # shell utilities useful for mocing and copying files

path = Path("ecommerce/__init__.py")
# path.exists() # check to see if it exists
# path.rename("test") # rename the file
# path.unlink() # delete the file
print(path.stat())
# st_size: File size in bytes
# st_atime= last access time in epoch
# st_mtime= last modified time in epoch
#st_ctime= creationtime in epoch

# to show in human readeable time"
print(ctime(path.stat().st_ctime))

print(path.read_bytes())  # returns content of the file as Byte
print(path.read_text())  # returns content of the file as string

# However using path to copy or moving a file is tedious, here you use the shutil
source = Path("ecommerce/__init__.py")
target = Path()/"__init__.py"

# bad:
target.write_text(source.read_text())

# good: much cleaner
shutil.copy(source, path)
