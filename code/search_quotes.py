#!/usr/bin/env python

from typing import Optional
import argparse
import re
from pathlib import Path

# + is greedy (captures as many chars as it wants)
# +? is non greedy (captures fewest amount of chars)
# We need non greedy or else .+ portion will capture all contents
#   up until the last header in the file.
PATTERN = r"(?:.*?[Qq]uotes.*?\n)(?:^(?:-|=){3,}$\n)((?:.*?\n)+?)(?:(?:(?:.*?\n)(?:-|=){3,}))"
# TODO: This pattern will not capture quotes if Quotes is the last header in the file.

def parse_options() -> dict:
    parser = argparse.ArgumentParser(description = 'Search folder recursively for regex pattern.')
    parser.add_argument('--path', dest='folder_path', type=str, help='A folder to search.')
    parser.add_argument('--regex', dest='pattern', type=str, default=PATTERN, help='Regex pattern to match.')
    return parser.parse_args()

def is_markdown(file_path: Path) -> bool:
    return file_path.suffix == '.md'

def file_contents(file_path: Path) -> str:
    with open(file_path, 'r') as f:
        return f.read()

def search_recursively(folder_path: Path, regex: re.compile) -> dict:
    results = {}
    files_to_search = list(folder_path.glob('**/*.md'))
    for file_to_search in files_to_search:
        found_text = search_file(file_to_search, regex)
        if found_text:
            results[f"{file_to_search.resolve()}"] = found_text
    return results

def parse_contents_for_pattern(regex: re.compile, contents: str) -> str:
    result = ""
    matches = re.search(regex, contents)
    if matches:
        for group in matches.groups():
            result = result + f"{group}\n"
    return result

def search_file(file_path: Path, regex: re.compile) -> Optional[str]:
    contents = ""
    if not is_markdown(file_path):
        return None
    else:
        contents = file_contents(file_path)
        return parse_contents_for_pattern(regex, contents)

if __name__ == "__main__":
    args = parse_options()
    if folder_path_str := args.folder_path:
        folder_path = Path(folder_path_str)
    else:
        folder_path = Path.cwd()

    if pattern_string := args.pattern:
        regex = re.compile(pattern_string, flags=re.MULTILINE)
    else:
        regex = re.compile(PATTERN, flags=re.MULTILINE)
    print(f"Searching `{folder_path}` for Quotes")
    print(f"based on this regex pattern: \n{regex.pattern}")
    results = search_recursively(folder_path, regex)
    for _,v in results.items():
        print(f"{v}")
