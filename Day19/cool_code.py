print("\033c")

print("\t\033[35;1;6;4;5mBest Wednesday Ever!\033[0m\n")


from dis import dis
import opcode

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # the Context
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<{}'s Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.customer.name, self.total(), self.due())


import inspect


import promotions
from promotions import *

def best_promo(order):
    promos = [func for name, func in
                    inspect.getmembers(promotions, inspect.isfunction)]

    # promos = [
    #     globals()[func]
    #     for func in globals()
    #     if func.endswith("_promo") and func != "best_promo"
    # ]
    return max(promo(order) for promo in promos)


joe = Customer("John Doe", 0)
ann = Customer("Ann Smith", 1100)
cart = [
    LineItem("banana", 4, 0.5),
    LineItem("apple", 10, 1.5),
    LineItem("watermellon", 5, 5.0),
]
banana_cart = [LineItem("banana", 30, 0.5), LineItem("apple", 10, 1.5)]


print(Order(ann, cart, best_promo))
print(Order(joe, banana_cart, best_promo))
print(Order(joe, cart, fidelity_promo))

print(Order(ann, cart, fidelity_promo))
print(Order(ann, cart, large_order_promo))
print(Order(joe, banana_cart, bulk_item_promo))
