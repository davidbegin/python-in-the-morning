import pytest
import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write

    yield

    sys.stdout.write = original_write




class LookingGlass():
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, a,b,c):
        import sys
        sys.stdout.write = self.original_write


# DON'T UPDATE THISSSSSSS
def reverso():
    with looking_glass() as what:
        return print("Alice, Kitty and Snowdrop")


def test_looking_glass(capsys):
    reverso()
    captured = capsys.readouterr()
    assert captured.out == "pordwonS dna yttiK ,ecilA\n"
