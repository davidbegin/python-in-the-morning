#!/usr/bin/env python


import os
from typing import Optional
import argparse
import re
from pathlib import Path

# Goal:
#      - Create more default patterns for other categories
#      - Strip out some white space
#      - VERBOSE mode and refactor experessions

# + is greedy (captures as many chars as it wants)
# +? is non greedy (captures fewest amount of chars)
# We need non greedy or else .+ portion will capture all contents
#   up until the last header in the file.
QUOTES_PATTERN = (
    r"(?:.*?[Qq]uotes.*?\n)(?:^(?:-|=){3,}$\n)((?:.*?\n)+?)(?:(?:(?:.*?\n)(?:-|=){3,}))"
)

DEBATES_PATTERN = (
    r"(?:.*?[Dd]ebates.*?\n)(?:^(?:-|=){3,}$\n)((?:.*?\n)+?)(?:(?:(?:.*?\n)(?:-|=){3,}))"
)

HEADER_SEARCHES = {
    "quotes": QUOTES_PATTERN,
    "debates": DEBATES_PATTERN
}

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
        default=QUOTES_PATTERN,
        help="Regex pattern to match.",
    )
    parser.add_argument(
        "--header",
        dest="header",
        type=str,
        help="Header to match on",
    )
    return parser.parse_args()


# Can we refactor this
def parse_contents_for_pattern(regex: re.compile, contents: str) -> str:
    result = ""
    if matches := re.search(regex, contents):
        for group in matches.groups():
            result = result + f"{group}\n"
    return result


# Can we refactor this
def search_recursively(folder_path: Path, regex: re.compile) -> dict:
    results = []
    
    for file_to_search in folder_path.glob("**/*.md"):
        if found_text := parse_contents_for_pattern(regex, file_to_search.read_text()):
            results.extend(
                    [ result for result in found_text.split("\n\n") if result.strip() ]
            )
    return  results


# lines = bigstring.split()
# lines = [line for line in lines if line.strip()]

if __name__ == "__main__":
    args = parse_options()
    folder_path = args.folder_path
    if args.header:
        regex = re.compile(HEADER_SEARCHES[args.header], flags=re.MULTILINE)
    else:
        regex = re.compile(args.pattern, flags=re.MULTILINE)

    if "DEBUG_MODE" in os.environ:
        print(f"Searching `{folder_path}` for Quotes")
        print(f"based on this regex pattern: \n{regex.pattern}")

    results = search_recursively(folder_path, regex)

    for r in results:
        print(f"{r}")
