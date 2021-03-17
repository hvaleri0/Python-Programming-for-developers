import setuptools
from pathlib import Path

setuptools.setup(
    name="moshpdf",
    version=1.0,
    # Automatically extract descrition from the README.md file

    long_description=Path("README.md").read_text(),
    # Automatically detects the packages in the folder but exclude the tests and data folder:
    packages=setuptools.find_packages(exclude=["tests", "data"])
)
