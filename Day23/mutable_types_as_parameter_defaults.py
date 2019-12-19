print('\033c')

print("\t\033[35;1;6;4;5mBest Wednesday Ever! \033[0m\n")


from dis import dis
import opcode




class HauntedBus:
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return f"{id(self)} - {self.passengers}"


b1 = HauntedBus(["begin"])
b2 = HauntedBus()
b2.pick("bill evans")
b3 = HauntedBus()

print(b3)
