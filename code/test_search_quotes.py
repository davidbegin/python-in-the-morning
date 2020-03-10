from pathlib import Path
import re

import pytest

from search_quotes2 import search_recursively, QUOTES_PATTERN


def test_make_sure_quotes_didQUOTES__not_change():
    regex = re.compile(QUOTES_PATTERN, flags=re.MULTILINE)
    # Path(__file__).resolve().parent

    raw_quotes = Path().cwd().joinpath("code/expected_quotes.txt").read_text()

    expected_quotes = [quote for quote in raw_quotes.split("\n\n")]

    output = search_recursively(Path.cwd().resolve(), regex)
    assert len(output) == len(expected_quotes)
    # breakpoint()
    # for o, e in zip(output, expected_quotes):
    #     if o != e:
    #         print(f"o: {o}")
    #         print(f"e: {e}")
    #         print("-----")
    # breakpoint()

    # print(expected_quotes)
