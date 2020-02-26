import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 1000000

SETUP = """
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


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
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())



def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0



def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    return sorted([
        fidelity_promo(order),
        large_order_promo(order),
        bulk_item_promo(order)
    ])[-1]


promos = [
    fidelity_promo,
    large_order_promo,
    bulk_item_promo
]


def better_best_promo(order):
    return max(promo(order) for promo in promos)

def best_promo(order):
    return sorted([
        fidelity_promo(order),
        large_order_promo(order),
        bulk_item_promo(order)
    ])[-1]

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [
    LineItem('banana', 4, .5),
    LineItem('apple', 10, 1.5),
    LineItem('watermellon', 5, 5.0)
]
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


clock("best_promo()       : ", "Order(ann, cart, best_promo)")
clock("better_best_promo(): ", "Order(ann, cart, better_best_promo)")


