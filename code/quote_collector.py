from pathlib import Path
import re


def read_all_files():
    root_dir = Path(__file__).parent.parent
    for path in root_dir.glob("**/*"):
        print(path)


def reg101():
    # Do I need the * to match the whole file?
    # is this needed because we are using `r` aka raw string ?
    # what is ?: in the reg world

    # (?:-{3,}|={3,}\n)
    # [-=]{3,}\n

    # (?:-{3,}|={3,}\n)
    # ---
    # ===

    # 3 or more of whatever is ever is before
    # {3,}

    # (?:-{3,}|={3,}\n)

    regex = r"(?:Quotes?).*\n[-=]{3,}\n((?:.*\n)*)(?=.*\n)[-=]{3,}\n"
    # regex = r"Quotes\n[-=]*\n*((?:.*\n*)*)[---|===]*"

    # regex = r"Quotes\n[-=]*\n*((?:.*\n*)*)[---|===]*"

    test_str = (
        "Quotes\n"
        "-------\n\n"
        "Life is Good\n\n"
        "Life is Pain\n\n"
        "Scraps\n"
        "------"
    )

    # This implies -g /g
    matches = re.finditer(regex, test_str, re.MULTILINE)

    for match_num, match in enumerate(matches, start=1):
        print(f"Match: {match}")

        # print("Match {match_num} was found at {start}-{end}: {match}".format(match_num = match_num, start = match.start(), end = match.end(), match = match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            # print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


def collect_quotes():
    test_file = "Fluent_Python/Day45/README.md"
    quote_file = Path(__file__).parent.parent.joinpath(test_file)
    text_to_search = quote_file.read_text()

    # regex_str = 'Quotes\n(-|=)*\n*(---|===)*'
    regex_str = r"Quotes\n[-=]*\n*(.*\s*.*)[---|===]"
    regex_str = r"Quotes\n[-=]*\n*(.*\s*.*)[---|===]*"
    quotes_search = re.compile(regex_str)

    result = quotes_search.match(text_to_search)
    print(result)
    # breakpoint()

    # with open(quote_file) as f:
    #     print(f.read())


if __name__ == "__main__":
    # collect_quotes()
    reg101()
    read_all_files()
