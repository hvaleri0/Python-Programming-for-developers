# Unpythonic:
class Product_Unpythonic:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = price

    price = property(get_price, set_price)

# pythonic:
# you can hide the seeters and getter by making private but there is a much better solution by using decorators


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = price


# results unpyhthonic
product = Product_Unpythonic(50)
# notice if its negative it throws an exception
# Product_Unpythonic.price = -1


# pythonic
newproduct = Product(50)
print(newproduct.price)
