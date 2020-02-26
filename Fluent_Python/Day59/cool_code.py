print('\033c')


from dis import dis
import opcode


class Validator:
    def __init__(self, func, value):
        self.func = func
        self.__set__(None, value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if self.func(value):
            self.value = value
        else:
            raise ValueError(f"value ({value}) did not pass the validator")


# EXAMPLE


class Person:
    def __init__(self, age):
        age = Validator(lambda age: age >= 0, age)


me = Person(12)

print(Person.age)
# me.age = -2



