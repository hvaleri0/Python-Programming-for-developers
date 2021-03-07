# Two types of import :absolute and relative
# absolute:
from ecommerce.customer import contact

# relative:
from ..customer import contact
# "." current folder , ".." one level up

# recommended to use absolute based on PEP-8 but if it gets too verbose eg. a.b.c.e... then use relative

contact.contact_customer()


def calc_tax():
    pass


def calc_shipping():
    pass
