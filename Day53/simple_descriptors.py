


# ```
# descr.__get__(self, obj, type=None) -> value
#
# descr.__set__(self, obj, value) -> None
# ```


class DataDescriptor:
    def __set__(self, obj, value):
        print("WHAT IS GOING ON")
        return "THIS IS FROM THE DESCRIPTION"


class NonDataDescriptor:
    pass

    # def __set__(self, obj, value):
    #     return "HELLo"

    # def __get__(self, obj, type=None):
    #     pass


class Person():
    cls_attr = "A Class ATTR"
    # name = DataDescriptor()
    name = NonDataDescriptor()

    def __init__(self):
        self.name = "A NAME"
        self.data_des = "DATA Descriptor"
        self.nondata_des = "NONT data Descriptor"


p1 = Person()
print(f"p1.name: {p1.name}")
# breakpoint()


