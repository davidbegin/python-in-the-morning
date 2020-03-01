print('\033c')

print("\t\033[35;1;6;4;5m InsertDayAndHopesAndDreams!\033[0m\n")


from dis import dis
import opcode

# When you are writing metaclasses, is it typically just the new method
class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print(cls, name, bases, body)
        return super().__new__(cls, name, bases, body)

# Library maintainer created this
# need to ensure some interface
class Foo():
    def bar(self):
        return "bar"
    
    def hello():
        i,,,
    
    def __init_subclass__(cls, default_name):
        print(f"__init_subclass__ time! {default_name}")

class Derived(Foo, default_name="begin"):
    def baz(self):
        breakpoint()
        return self.bar() + "baz"

# ===

class Philosopher:
    def __init_subclass__(cls, /, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name

class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass
