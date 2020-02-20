
def auto_meta(cls):
    class new_cls(metaclass=cls):
        pass

    return cls


@auto_meta
class TestingMeta(type):
    def __new__(cls, *args, **kwargs):
        cls = type.__new__(cls, *args, **kwargs)
        print(f"created class {cls.__name__}")
        return cls


class SomeClass(TestingMeta):
    pass
