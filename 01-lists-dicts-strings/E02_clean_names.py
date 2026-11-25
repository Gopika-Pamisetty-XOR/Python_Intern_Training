#Problem
#"Names typed by users are messy. Write clean_name(raw) that removes leading and trailing spaces, collapses repeated inner spaces to one space, and converts to title case. Write initials(name) that returns the initials separated by dots, for example "Anna Maria Smith" gives "A.M.S.". For each raw name print the cleaned name (with repr, so quotes are visible) and its initials."


def clean_names(raw):
    return " ".join(raw.split()).title()


def initials(name):
    result= " "
    # print(name,"name")
    for word in name.split():
        # print(word, "word")
        # print(word[0],"word[0]")
        result+= word[0] + "."
        # print("result: ",result)
    return result




names = [
    "  aNNa   maRIA  smith ", 
    "o'brien   john", "MARY-JANE watson", 
    "li   wei"
]

for raw in names:
    cleaned = clean_names(raw)
    print(f"{cleaned} -> {initials(cleaned)}")
