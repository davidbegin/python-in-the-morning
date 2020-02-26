print('\033c')

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

promos = []

def promotions(func):
    print(f"Registering Promotion: {func}")
    promos.append(func)
    return func

@promotions
def fidelity_promo(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


@promotions
def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


@promotions
def large_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0




# We want a list of promos that can be applied to orders
# We also want a way for program to pick the best promo
# We can define a new Promotion
# How do we know to evaluate the new Promotion when
# looking for the best promo


def best_promo(order):
    # promos = [func for name, func in
    #                 inspect.getmembers(promotions, inspect.isfunction)]

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
