import pytest

class LookingGlass():
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


# DON'T UPDATE THIS
def reverso():
    with LookingGlass() as what:
        return print("Alice, Kitty and Snowdrop")


def test_looking_glass(capsys):
    reverso()
    captured = capsys.readouterr()
    assert captured.out == "pordwonS dna yttiK ,ecilA\n"
