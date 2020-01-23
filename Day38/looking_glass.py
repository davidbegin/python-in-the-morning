import pytest

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
    with LookingGlass() as what:
        return print("Alice, Kitty and Snowdrop")


def test_looking_glass(capsys):
    reverso()
    captured = capsys.readouterr()
    assert captured.out == "pordwonS dna yttiK ,ecilA\n"
