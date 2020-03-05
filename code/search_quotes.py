#!/usr/bin/env python


# ?: -> don't capture but lets use groups

# .*? -> non greedy grab anything

# Could we make the Quotes case insensitive
# Verbose Mode
# With comments of Whats it matching
# Quotes:
# --------:
# The meat of the quotes
# TITLE_PATTERN = r"(?:.*?[Qq]uotes.*?\n)"
# PATTERN = r"(?:.*?[Qq]uotes.*?\n)
# (?:^(?:-|=){3,}$\n)
# ((?:.*?\n)+?)
# (?:(?:(?:.*?\n)(?:-|=){3,}))"


from typing import Optional
import argparse
import re
from pathlib import Path

# + is greedy (captures as many chars as it wants)
# +? is non greedy (captures fewest amount of chars)
# We need non greedy or else .+ portion will capture all contents
#   up until the last header in the file.
PATTERN = (
    r"(?:.*?[Qq]uotes.*?\n)(?:^(?:-|=){3,}$\n)((?:.*?\n)+?)(?:(?:(?:.*?\n)(?:-|=){3,}))"
)
# TODO: This pattern will not capture quotes if Quotes is the last header in the file.

# We didn't we use Dict
def parse_options() -> dict:
    parser = argparse.ArgumentParser(
        description="Search folder recursively for regex pattern."
    )
    parser.add_argument(
        "--path",
        dest="folder_path",
        type=Path,
        default=Path().cwd(),
        help="A folder to search.",
    )
    parser.add_argument(
        "--regex",
        dest="pattern",
        type=str,
        default=PATTERN,
        help="Regex pattern to match.",
    )
    return parser.parse_args()


def parse_contents_for_pattern(regex: re.compile, contents: str) -> str:
    result = ""
    matches = re.search(regex, contents)
    if matches:
        for group in matches.groups():
            result = result + f"{group}\n"
    return result




# Do we want this to continue to just call read_text()
# the method name makes sense in the current contextr
# but why don't we just search text
# def search_file(file_path: Path, regex: re.compile) -> Optional[str]:
#     return parse_contents_for_pattern(regex, file_path.read_text())


# This is the main entry point of logic
# I would like that to be more obvious
# that would be through positioning
def search_recursively(folder_path: Path, regex: re.compile) -> dict:
    # Is there a way to do this without appending to a Dict
    results = {}
    
    # Why are creating the list right away?
    # How Pathlib biz!
    files_to_search = list(folder_path.glob("**/*.md"))
    
    # file_to_search might be a lil to long of var name
    # Poll:
    #   - Better var names
    for file_to_search in files_to_search:
        found_text = parse_contents_for_pattern(regex, file_to_search.read_text())
        if found_text:
            results[f"{file_to_search.resolve()}"] = found_text
    return results


if __name__ == "__main__":
    args = parse_options()
    folder_path = args.folder_path
    regex = re.compile(args.pattern, flags=re.MULTILINE)

    # Thanks for logging!
    print(f"Searching `{folder_path}` for Quotes")
    print(f"based on this regex pattern: \n{regex.pattern}")

    results = search_recursively(folder_path, regex)

    for _, v in results.items():
        # Why do we need an f-string, is it for implicit __repr__
        print(f"{v}")
