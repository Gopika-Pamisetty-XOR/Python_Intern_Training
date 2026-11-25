import re


def starts_with_number(text):
    return re.match(r"\d+", text) is not None


def first_number(text):
    match = re.search(r"\d+", text)
    if match:
        return int(match.group())
    return None


def is_whole_number(text):
    return re.fullmatch(r"\d+", text) is not None


samples = ["42 apples", "apples 42", "42", "forty-two", ""]

for text in samples:
    match_result = starts_with_number(text)
    search_result = first_number(text)
    fullmatch_result = is_whole_number(text)

    print(
        f"{text!r:<12} "
        f"match={match_result!s:<5} "
        f"search={search_result!s:<5} "
        f"fullmatch={fullmatch_result}"
    )