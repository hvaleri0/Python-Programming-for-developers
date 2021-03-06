import sales
from sales import calc_shipping, calc_tax
`  # method 1: import individual objects

# method 2: import entire module as an object

# importing all is bad practice because you can blindly import functions that can overwrite your intended ones:
#from sales import *

calc_tax()
calc_shipping


sales.calc_shipping()
