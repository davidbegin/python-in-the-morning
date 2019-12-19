print('\033c')

print("\t\033[35;1;6;4;5mBest Wednesday Ever! \033[0m\n")


from dis import dis
import opcode



class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind



import weakref

stock = weakref.WeakValueDictionary()

catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
                Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))

del catalog

print(sorted(stock.keys()))

del cheese

print(sorted(stock.keys()))
