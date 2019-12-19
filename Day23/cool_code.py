print('\033c')

print("\t\033[35;1;6;4;5mBest Wednesday Ever! \033[0m\n")


from dis import dis
import opcode




class TwilightBus:
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=None):
        if passengers:
            # self.passengers = passengers[:]
            self.passengers = list(passengers)
        else:
            self.passengers = []

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return f"{id(self)} - {self.passengers}"




class Person():
    pass


import weakref

def on_delete():
    print("I'm being deleted!")

a_set = Person()
# a_set = {0, 1}

weakref.finalize(a_set, on_delete)

wref = weakref.ref(a_set)

print(wref)
print(wref())

del a_set

print(wref())



# a_set = {2, 3, 4}
# wref()
# wref() is None
# wref() is None
