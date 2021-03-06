# this is tedious because you will have to use the dot notation to call a function everytime, instead import using from
import ecommerce.sales
# Using From
from ecommerce.sales import calc_shipping
# or if its too noisy and have alot of functions to import
from ecommerce import sales

ecommerce.sales.calc_shipping()
calc_shipping()
sales.calc_shipping
