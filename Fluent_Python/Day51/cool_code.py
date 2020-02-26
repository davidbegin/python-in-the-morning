print("\n\nin 2001 on this day the deadly Anna Kournikova virsus was unleashed on the world\n\n")


from dis import dis
import opcode

# __hasattr__
# __getattr__
# __setattr__

# these are all for setting attributes on an instance
# finally all attributes are stored in a __dict__, accessible self.__dict__
# if we interact with the __dict__, we bypass these special methodso

class Person:
    def __init__(self):
        print(f"Attributes: {self.__dict__}")

    # Not sure of all the times this is implicitly called
    def __hasattr__(self, name):
        print(f"We are if has hattrs! {name}")
        return super().__hasattr__(self, name)

    # Right here!
    def __getattr__(self, name):
        breakpoint()
        print(f"We are looking to get attrs! {name}")
        return super().__getattr__(self, name)


p1 = Person()

# invoking this, did invoke the __getattr__
p1.fake_attr
breakpoint()

print("The END")








