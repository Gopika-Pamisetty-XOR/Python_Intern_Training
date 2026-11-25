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