import pytest

# DON'T UPDATE THIS JUST CREATE A CONTEXT MANAGER
def reverso():
    with YOUR_CONTEXT_MANAGER as what:
        return print("Alice, Kitty and Snowdrop")


def test_looking_glass(capsys):
    reverso()
    captured = capsys.readouterr()
    assert captured.out == "pordwonS dna yttiK ,ecilA\n"
